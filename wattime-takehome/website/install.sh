#!/bin/bash
#build and deploy script
pid=$!
cname=cv.jnapolitano.io
RED='\033[0;31m'
PINK='\033[38;5;206m'
PURPLE='\033[1;95m'
JUSTIN='\033[38;5;206;48;5;57m'
UNICORN='\U1F984'
HEART='\xF0\x9F\x92\x9C'
BHEART='\xF0\x9F\x92\x94'
NC='\033[0m' # No Color
KISS='\xF0\x9F\x98\x98'
CWEEN='\xF0\x9F\x98\x8B'
PWEASE='\xF0\x9F\x98\xB3'
HOPE='\xF0\x9F\x98\x85'
HAPPY='\xF0\x9F\x98\x81'
ANGEL='\xF0\x9F\x98\x87'
BOSS='\xF0\x9F\x98\x8E'
KISSY='\xF0\x9F\x98\x99'
DEVIL='\xF0\x9F\x98\x88'
MAKEY='\xF0\x9F\x98\xAE'
MMM='\xF0\x9F\x98\x9B'
BIGCRY='\xF0\x9F\x98\xA2'
YAY='\xF0\x9F\x98\x81'
TWO_HEARTS='\xF0\x9F\x92\x95'
TOUNGEY='\xF0\x9F\x98\x9C'
PEACE='\xE2\x9C\x8C'
SHY='\xF0\x9F\x98\x93'
FEAR='\xF0\x9F\x98\xA8'
FLUSH='\xF0\x9F\x98\xB3'
THUMBS='\xF0\x9F\x91\x8D'
BEER='\xF0\x9F\x8D\xBA'
CHEERS='\xF0\x9F\x8D\xBB'
PYTHON='\xF0\x9F\x90\x8D'
EGGPLANT='\xF0\x9F\x8D\x86'
SHRIMP='\xF0\x9F\x8D\xA4'
MOON='\xF0\x9F\x8C\x9A'
GRIMACE='\xF0\x9F\x98\xAC'
STRONG='\xF0\x9F\x92\xAA'
OK='\xF0\x9F\x91\x8C'
CIGGI='\xF0\x9F\x9A\xAC'
EXHALE='\xF0\x9F\x92\xA8'
TASKS=6

sp[0]="${HEART}"
sp[1]="${BHEART}"
think[0]='.'
think[1]='.'
think[2]='.'

uWu[1]=u
uWu[2]=W
uWu[3]=u

# Define a timestamp function
timestamp() {
  date +"%T-%m-%d-%Y" # current time
}


introduction () {
    printf "${PURPLE}Hi ${FLUSH} I'm going to install some dependencies! ${PEACE} "

}


check_git () {
    printf "\n Second:"
    
    printf "\n  we have to check for git."
    
    if ! command -v git &> /dev/null
    then
        printf "${PURPLE}\n     oh nooooo! ${BIGCRY} I couldn't find git" 
        
        printf "Time to install it ${TOUNGEY}" 
        
        install_git

    else
        printf "${PURPLE}'\nYay! ${YAY} I found Git"
        
        printf "Nothing to install ${THUMBS}"
    fi

}

install_git () {
    printf "/n  Installing GIT.  Be patient ${CIGGIE}"
    command brew install git
    printf "\n  All good ${EXHALE}"
    
}
check_brew () {
    printf "\n First:"
    
    printf "\n  let's check for brew ${BEER}."
    
    if ! command -v brew &> /dev/null
    then
        printf "${PURPLE}\n     oh nooooo! ${BIGCRY} I couldn't find brew" 
        
        printf "Time to install it ${TOUNGEY}" 
        install-x-code
        printf "\n  Okay ${OKAY}, now we should be good"

    else
        printf "${PURPLE}'\n    Yay! ${YAY} I found brew ${CHEERS}"
        
        printf "Nothing to install ${THUMBS}"
    fi
}

install-x-code () {
    local check=$((xcode-\select --install) 2>&1)
    local str="xcode-select: note: install requested for command line developer tools"
    printf "Since you don't have brew"
    
    printf "Now I've gotta check for x-code"
    

    echo $check
    while [[ "$check" == "$str" ]];
    do
        osascript -e 'tell app "System Events" to display dialog "xcode command-line tools missing." buttons "OK" default button 1 with title "xcode command-line tools"'
        exit;  
    done
    
    printf "\n  X-code is installed.  You're cool ${BOSS} now"
    
    install-brew
    
}

install-brew () {
    printf "but now I have to run a download script for Brew.  Follow their prompts please ${PWEASE}"
    
    command /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

}

check_python () {
    printf "\n Third:"
    
    printf "\nChecking for python "
    printf "python  ${PYTHON}."
    if ! command -v python3 &> /dev/null
    then
        install_python

    else

        printf "Nothing to install ${THUMBS}"
    fi
}


install_python () {
    printf "/n  Installing Python.  Be patient ${CIGGIE}"
    command brew install python
    printf "\n  All good ${EXHALE}" 
}



check_virtualenv () {
    printf "\n Fourth:"
    
    printf "\n  We need to go to"
    
    printf "an isolated environment ${MOON}."
    
    if ! command -v virtualenv &> /dev/null
    then
        printf "${PURPLE}\noh nooooo ${BIGCRY} I can't make us a private environment ${GRIMACE}" 
        
        printf "Guess I've gotta make one ${STRONG}" 

    else
        printf "${PURPLE}'\n    Yay! ${YAY} We can make virtual environments ${OK}"
        
        printf "Nothing to install ${THUMBS}"
    fi
}

install_virtualenv () {
    printf "/n  Installing virtualenv.  Be patient ${CIGGIE}"
    command pip3 install virtualenv
    printf "\n  All good ${EXHALE}"
}
clean () {
    printf "${PURPLE}Cleaning old build  $HEART"
    command make clean > /dev/null
    printf "\n  All cween ${CWEEN}"

}

html () {
    printf "\nMaking your html files ${PWEASE}"
    command make html &> /dev/null
    printf "\n  Files Made ${HOPE}"
}
add () {
    printf "\nAdding changes ${HAPPY}"
    command git add . &>/dev/null
    printf "\n  Changes added"
}

commit () {
    printf "\nCommiting Changes ${ANGEL}"
    command git commit -m "autocommit on $(timestamp)" &>/dev/null
    printf "\n  Committed ${BOSS}"
}

push () {
    printf "\nPushing them files sir ${KISSY}"
    command git push  &>/dev/null 
    printf "\n  pushed the files${DEVIL}"
}

deploy () {
    printf "\n Making Website now ${MAKEY}"
    command ghp-import -n -p -f -c $cname build/html &>/dev/null 
    printf "\n Site is live at $cname"
}

progress () {
    i=0
    while kill -0 $pid 
    do
        i=$(( (i+1) %2 ))
        printf "${spin{$i}}"
        sleep .5
    done
}
fakeProgress () {
    i=0
    j=0 
    while [ $j -le 5 ]
    do
        ((j++))
        i=$(( (i+1) %2 ))
        printf "${sp[$i]}"
        
        sleep .5
    done 
}
getpid () {
    pid=$!
}

spin() {
   printf "\b${sp:sc++:1}"
   ((sc==${#sp})) && sc=0
}
endspin() {
   printf "\r%s\n" "$@"
}

main () {
    introduction && check_brew && check_git && check_python && check_virtualenv
}

main
