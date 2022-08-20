.PHONY:test,run

run:
	python server.py

test:
	python test/test.py

git_a:
	git add --all

git_c:
	git commit -m "a"

git_t:
	git -a tag -m "a"

git_p:
	git push

git_p_t:
	git push --tags

git_l:
	git logs

git_s:
	git status

