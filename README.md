# GitGist

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

GitHub Gist API app to get any user's Gist contributions 

###  1. Search the user
![1](https://user-images.githubusercontent.com/81184255/210281653-d4b1119b-14a4-4954-9d70-da858cab09a9.jpg)

### 2. Each gist will have the last three fork owners displayed
![2](https://user-images.githubusercontent.com/81184255/210282348-7b535d4e-8abe-4639-b68e-9e170333f8f3.jpg)

### 3. When clicked, the gist will show the code content along with a GitHub-like language tag
![3](https://user-images.githubusercontent.com/81184255/210282386-ad0c5b12-88d2-40d5-8474-077635b11a9d.jpg)

> **Warning**
> Sometimes the GitHub Gist API will reach its limit (60 request/h/ip) :P

To check your status, use this:

```bash
curl -I https://api.github.com/users/YourUserName
```

> **Note**
> This will give you the Unix time for your reset limit like this:

```
X-RateLimit-Reset: 1672698829
```

You can then use an epoch time stamp converter like [this one](https://www.unixtimestamp.com/) to get the relative time.


