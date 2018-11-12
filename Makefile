.PHONY: serve build

HOST=pyparis.org

build:
	# ./pyparis-to-talks.py
	./scripts/gen_prog.py
	yarn run wintersmith build

serve:
	yarn run wintersmith preview

zip:
	zip -r contents/static/pdf/all-slides.zip slides

deploy: build
	rsync -e ssh -avz build/ websites@${HOST}:/home/websites/pyparis2018/

clean:
	rm -rf build
	find . -name "*.pyc" | xargs rm -f

#serve:
#	cd src ; python -m SimpleHTTPServer 8000

