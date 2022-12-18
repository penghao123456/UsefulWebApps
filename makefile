GIT=git
ADD=add
COMMIT=commit
PUSH=push
BRANCH=$(shell git branch | grep -E "^\* .+" -o | grep -E "[^* ]+" -o)

commit:* .gitignore
	-$(GIT) $(ADD) $^ .gitignore
	-$(GIT) $(COMMIT)

push:commit
	$(GIT) $(PUSH) origin $(BRANCH)
