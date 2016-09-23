from fabric.api import local

def djangocom():
    local("./manage.py makemigrations")
    local("./manage.py migrate")

def gitcom():
	local("git status") 
	local("git add .")
	local("git commit -m 'via fabric' ")
	local("git push origin master")   