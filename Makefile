dump_dependencies:
	pip3 freeze > requirements.txt

install_dependencies:
	pip3 install -r requirements.txt
	sudo pacman -Syu imagemagick ffmpeg pdftk