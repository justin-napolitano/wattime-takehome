#!/bin/zsh
#build and deploy script
pid=$!
cname=freight.jnapolitano.io
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
TASKS=6



# Define a timestamp function
timestamp() {
  date +"%T-%m-%d-%Y" # current time
}



clean () {
    printf "${PURPLE}Cleaning the Least Build"
    command make clean > /dev/null
    printf "\n  All clean"

}

html () {
    printf "\nMaking your html Files"
    command make html > /dev/null
    printf "\n  Html Complete"
}
add () {
    printf "\nAdding changes"
    command git add . &>/dev/null
    printf "\nAdded Changes"
}

commit () {
    printf "\nCommiting those changes"
    command git commit -m "autocommit on $(timestamp)" &>/dev/null
    printf "\n  Committed "
}

push () {
    printf "\nPushing files."
    command git push  &>/dev/null
    printf "\n Pushed"
}

deploy () {
    printf "\n Making website now ${MAKEY}"
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

checkout () {
    command git checkout gh-pages
}

remove_all () {
    command sudo rm -r *
}

checkout_main () {
    command git checkout main
}

clean-gh-pages () {
    printf "\n Cleaning gh-pages now"
    checkout && remove_all && add && commit && push && checkout_main
}
add && commit && push && clean-gh-pages && deploy

