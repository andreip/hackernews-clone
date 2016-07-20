Planning proposal
---

- Pages it will contain:
  - /home
    - displays the feed news where logged in people can upvote
    - a profile username link and a logout to the top right
    - a footer for Contact, API, RSS, Guidelines, FAQ
    - a way to paginate through results ; next/previous page at top and bottom
    - when user comments/upvotes, keep track of all his actions
      - possibility to extend it to offer recommendations in the digest, even the ones that aren't
        that much upvoted
  - /login
    - create account
    - login with google
    - login with facebook, twitter
  - /profile
    - (default) receive daily digest via email notifications
    - set personal info
  - /api
    - /api/posts GET only
      - offers meta info about a post: pubdate, #upvotes, link, title, #comments, a list of users implicated in thread (commented)
    - /api/users GET only
      - returns the users by pk

- Bootstrap with some articles:
  - to start off, it'd be nice to pull some content from somewhere; HN API, reddit, HN rss feeds?
  - maybe generate random comments by some users
