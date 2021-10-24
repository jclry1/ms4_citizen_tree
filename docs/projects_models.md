
[Back to README](../README.md#design---database)

The main content of the site is managed by two models - one for projects and one for updates. These have connections one to the other and both also have a foreign key relationship to the custom user model:
![Project, Update, User Models](/docs/readme_images/project_update_user_models.png)