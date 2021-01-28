from github import Github
# doc for lib https://pygithub.readthedocs.io/en/latest/introduction.html

ACCESS_TOKEN = 'your_token'  # find that here: tinyurl.com/yx9l23cp

g = Github(ACCESS_TOKEN)  # init client

# use for testing connection. Comment out after
# if successful should see something like:
# <github.PaginatedList.PaginatedList object at ..........>
#print(g.get_user().get_repos())


# nitty gritty
def search_github(keywords):
    # first take all keywords and split
    keywords = [keyword.strip() for keyword in keywords.split(',')]

    # API has limits
    # limit for unauth user - 60/hour
    # limit for auth user - 5000/hour
    # so knowing that, how do separate??
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate_limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')

    query = '+'.join(keywords) + '+in:readme+in:description+in:file'
    result = g.search_repositories(query, 'updated', 'desc')
    result2 = g.search_commits(query, 'committer-date', 'desc')
    result3 = g.search_code(query, order='desc')  # desc - highest matches, asc - lowest

    # results 1 and 2, 3 is below due to differences
    print(f'Found {result.totalCount} repo(s) mentioning {keywords}')
    print(f'Found {result2.totalCount} commit(s) mentioning {keywords}')

    for repo in result:
        print(repo.clone_url)

    for commit in result2:
        print(commit.author, commit.files, commit.url)

    # result3 can return a ton of stuff, which makes the GH gods angry. So we limit
    max_size = 500  # you CAN go over but honestly, don't
    print(f'Found {result3.totalCount} files containing {keywords}')
    if result3.totalCount > max_size:  # if grtr than max_size, limit to first 200
        result3 = result3[:max_size]

    with open('export.txt', 'w+') as f:
        for code in result3:
            '''You have a few options here:
            url: kinda useless, just shows json
            html_url: useful, shows the page
            git_url: not terribly useful
            download_url: really just shows plain text what's in the thing
        
            By far, html_url is the most useful'''
        #print(code.html_url)
            f.write(code.html_url + '\n')


# drive
if __name__ == '__main__':
    keyword = input('Enter keyword(s) separated by comma[e.g. python,node,ruby]: ')
    search_github(keyword)

# TODO: pipe results to a file?
# TODO: look more into rate limits and figure out how to handle that
# TODO: github shows 2k+ in code but this only shows 1k? why?
