mandoc = { debug = nil, todo = {}, count = 0, limit = 16 } -- package

function _log(...)
	if mandoc.debug and posix.getenv("VERBOSE_FILETRIGGERS") then
		print(mandoc.debug .. ": ", ...)
	end
end

function mandoc._run(add, file)
	if add then op = "-d" else op = "-u" end
	_log("calling makewhatis " .. op .. " " .. file)
	rpm.execute("/usr/sbin/makewhatis", op, "/usr/share/man", file)
end

function mandoc._handle(add, file)
        if not string.match(file, "/usr/share/man/man[^/]+/[^/]+.gz$") then
		return
	end
	if not posix.access(file) then
		return
	end
--	if mandoc.count < mandoc.limit then
		if add then
			_log("adding " .. file)
		else
			_log("removing " .. file)
		end
		mandoc.todo[file] = add
--	elseif mandoc.count == mandoc.limit then
--		_log("too many files, using makewhatis for batch processing")
--	end
	mandoc.count = mandoc.count + 1
end

function mandoc.add(fn)
	mandoc._handle(true, fn)
end

function mandoc.remove(fn)
	mandoc._handle(false, fn)
end

function mandoc.done()
	if mandoc.count < mandoc.limit and posix.access("/usr/share/man/mandoc.db") then
		for file, what in pairs(mandoc.todo) do
			mandoc._run(what, file)
		end
	else
		_log("calling makewhatis")
		rpm.execute("/usr/sbin/makewhatis")
	end
end
