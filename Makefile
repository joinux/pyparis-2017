.PHONY: serve build

build:
	./node_modules/.bin/wintersmith build

serve:
	./node_modules/.bin/wintersmith preview

zip:
	zip -r contents/static/pdf/all-slides.zip slides

deploy: build
	fab deploy

clean:
	rm -rf build

#serve:
#	cd src ; python -m SimpleHTTPServer 8000

