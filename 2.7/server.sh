cd ./Webpage;
printf "\n\nGo to the following link:\nfile://";
link=`pwd`;
printf "$link";
printf "/index.html\n\n\nStarting websocket server.\nPress control+c to exit. Do not use control+c to copy!";
cd ../Server;
python2 server.py;