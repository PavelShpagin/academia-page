# GitHub Pages deploy

This is a static site (plain HTML/CSS/JS). It can be hosted on GitHub Pages.

## Publish

1) Create a new GitHub repo (example name: `web_test`)

2) In this folder, run:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO>.git
git push -u origin main
```

3) In GitHub:
- **Settings → Pages**
- **Build and deployment → Source**: select **GitHub Actions**

After the Actions workflow finishes, your site will be live.

## Your GitHub Pages link

- Project pages: `https://<YOUR_GITHUB_USERNAME>.github.io/<YOUR_REPO>/`



