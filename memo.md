
# New Knowledge

## Git
### clone to local PC
```
git clone your-ssh-link-here
```
### if local PC has the same clone
#### replace
```
mv basic-automation basic-automation-old
```
#### delete 
```
rm -rf basic-automation
```

## Virtual Environment
It can isolate from local PC Env. Easy managing version and sharing with other developers.
### How to use
```
python -m venv myenv
source myenv/Scripts/activate  # On Windows
```
### Is VM included .gitignore?
Yes. But leave the file "requirements.txt" as a VM blueprint

###  requirements.txt
#### How to make requirements.txt?
- activate the vm
```
source myenv/Scripts/activate  # activate the vm
pip freeze > requirements.txt # make the file
deactivate # deactivate the vm

# echo $VIRTUAL_LAW # to check if the vm activated. If it is, (vm name) appeared
```
#### How other developers activate using my VM blueprint?
```
python -m venv myenv # Create a virtual environment
source myenv/bin/activate # Activate the virtual environment (On Windows, use `myenv\Scripts\activate`)
pip install -r requirements.txt # Install the dependencies
```



