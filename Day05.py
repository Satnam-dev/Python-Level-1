# Git Hub
# git --version
# git version 2.39.5 (Apple Git-154)


# To uplode code in git
# Step 1 :- git config --global user.email
# Step 2 :- git config --global user.name
# Step 3 :- git config --list
# Step 4 :- git status
# Step 5 :- git init
# Step 6 :- git add .
# Step 7 :- git commit -m "Today is my 7th day"
# Step 8 :- git push


# if want to add origin link in git hub
# git remote add origin (Paster link of that code from git hub)

# To delete or change repository
# git remote remove origin 
# git remote add origin (Paster link of that code from git hub)


# Transfer code from remote to locallly
# Used to pull git projets from any other git hub
# Step 1 :- git config --global user.email
# Step 2 :- git config --global user.name
# Step 3 :- git config --list
# Step 4 :- git init 
# Step 5 :- git remote add origin (Paster link of that code from git hub)
# step 6 :- git pull origin main

# other way 
# git init
# git clone

# git clone (Clone always first)
# cd backend/frontend 
# npm install
# npm run dev 
# if npm run dev not work 
# rm -rf node_modules package-lock.json
# npm cache clean --force 
# npm install
# npm run dev

# Open Backend folder and create.env file
# # copy env file 
# MONGODB_URL=(shared database for group but can be different your friend need to pull your updates)
# GROQ_API_KEY= (each person ow key)
# same port number like 6000 and so on

# To Update on git 
# git init 
# git add .
# git commit -m "Comment"
# git push origin main


# Pull if he update somethiing
# git init
# git remote add origin (Paster link of that code from git hub)
# git pull origin main


# if your foldername (frontend or backend)may be Submodule
# git rm --cached (folder name)
# rm -rf .git/modules/(folder name)
# git add folder name
# git commit -m "Comment"
# git push origin main

# cmmd + shift + p


# Collaboration:- It is a process where two or more people work together to achieve a common goal
# another can't add the code in your repository without your permission.
# You can give permission to another person to add the code in your repository by adding them as a collaborator in your repository.


# IMPORTANT
# git rm --cached Bachend/.env
# echo "Backend/.env" >> .gitignore
# touch .gitignore
# node_modules = It is very large and can recreate it by running npm install command. So, we don't need to upload it in git hub. So, we can add it in
# Backend/.env = It is used to store environment variables. So, we don't need to upload it in git hub
# .env = It is also used to store environment variables
# .DS_Store = It is a hidden file that is created by macOS to store custom attributes of a folder. So, we don't need to upload it in git hub