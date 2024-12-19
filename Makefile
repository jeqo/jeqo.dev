.PHONY: test
test:
	zig build serve -Dinclude-drafts=true
