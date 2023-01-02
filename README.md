# FlaskGist

Flask GitHub API app to get any user's Gist contributions 

## Search the user
![1](https://user-images.githubusercontent.com/81184255/210281463-0195b858-4cf0-48f7-84f1-dcf006c40613.jpg)

## Each gist will have the last three fork owners displayed
![2](https://user-images.githubusercontent.com/81184255/210280577-e025ac1f-ab88-48f9-a500-9aebbde522a1.jpg)

## When clicked, the gist will show the code content along with a GitHub-like programming language tag
![3](https://user-images.githubusercontent.com/81184255/210280583-fe343958-e03d-41b1-a4ea-78af0eb64011.jpg)

> **Warning**
> Sometimes the GitHub APi will reach its limit (60 request/h/ip).

To check your status, use this:

```bash
> curl -I https://api.github.com/users/YourUserName
```

> **Note**
> This will give you the Unix time for your reset limit like this:

```
X-RateLimit-Reset: 1672698829
```

You can then use an epoch time stamp converter like [this one](https://www.unixtimestamp.com/) to get the relative time.


