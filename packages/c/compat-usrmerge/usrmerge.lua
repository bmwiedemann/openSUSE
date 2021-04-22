usrmerge = { debug = nil } -- package

require("usrmerge_files")

-- for testing outside rpm
if posix == nil then
	posix = require("posix")
	function _symlink(old, new)
		os.execute("ln -vs " .. old .. " " .. new)
	end
	posix.symlink = _symlink
end

function _log(msg)
	if usrmerge.debug then
		print(usrmerge.debug .. ": " .. msg)
	end
end

function rootpath(path)
	_, _, p = string.find(path, "^/usr(/.*)")
	return p
end

function dirname(path)
	_, _, d, b = string.find(path, "^(.*)/([^/]*)")
	return d
end

function usrmerge._add(rp, relpath)
	if not usrmerge_files[rp] then return end
	if posix.stat(dirname(rp), "type") ~= "directory" then return end

	createit = false
	t = posix.stat(rp, "type")
	if t == nil then
		createit = true
	elseif t == "link" then
		dst = posix.readlink(rp)
		if dst ~= relpath then
			_log(rp .. ": fixing incorrect symlink (" .. dst .. " -> " .. relpath)
			os.remove(rp)
			createit = true
		end
	else
		_log(rp .. " exist but is no link, skipping")
	end
	if createit then
		_log("creating " .. rp .. " -> " .. relpath)
		posix.symlink(relpath, rp)
	end
end

function usrmerge.add(path)
	rp = rootpath(path)
	usrmerge._add(rp, ".." .. path)
end

-- if a legacy package with a file in /bin gets upgraded, it would
-- remove the link/file in /bin on uninstall. So we have to check
-- there and restore.
function usrmerge.add_postun(rp)
	if posix.stat("/usr" .. rp, "type") then
		usrmerge._add(rp, "../usr" .. rp)
	end
end

-- needed for the build system to install all links of packages that got
-- installed via rpm2cpio so didn't call triggers
function usrmerge.addexisting()
	for rp in pairs(usrmerge_files) do
		usrmerge.add_postun(rp)
	end
end

function usrmerge.remove(path)
	rp = rootpath(path)
	if not usrmerge_files[rp] then return end
	if posix.stat(dirname(rp), "type") ~= "directory" then return end

	t = posix.stat(path, "type")
	if t then
		_log(path .. " still exists, skipping")
		return
	end

	t = posix.stat(rp, "type")
	if t == "link" then
		relpath = ".." .. path
		dst = posix.readlink(rp)
		if dst == relpath then
			_log("remove " .. rp .. " -> " .. relpath)
			os.remove(rp)
		else
			_log(rp .. " incorrect link (".. dst .."), skipping")
		end
	elseif t then
		_log(rp .. " exist but is no link (".. t .."), skipping")
	end
end

function usrmerge.migrate(d)
	local errors = 0
	for i, name in ipairs(posix.dir(d)) do
		if name ~= '.' and name ~= '..' then
			local p = d .. "/" .. name
			local up = "/usr" .. p
			local t = posix.stat(p, "type")
			local ut = posix.stat(up, "type")
			if ut == nil or (ut == "link" and t ~= "link") then
				local f = posix.link
				if t == "directory" then
					-- can't hardlink dirs so move it
					f = posix.rename
				end
				if ut ~= nil then
					_log(" removing " .. up)
					posix.unlink(up)
				end
				local ok, err, e = f(p, up)
				if ok == nil then
					print("FAILED " .. p .. " -> " .. up .. ": " .. err)
					errors = errors + 1
				else
					_log(p .. " -> " .. up)
				end
			else
				if t == "directory" then
					print("BAD " .. p .. " is a directory but " .. up .. "exists")
					errors = errors + 1
				else
					_log("skipped " .. p)
				end
			end
		end
	end
	if errors > 0 then
		print("have to continue despire errors")
	end
	local ok, err, e = posix.rename(d, d .. ".merged")
	if ok == nil then
		print("FAILED to move " .. d .. " out of the way")
	else
		ok, err, e = posix.symlink("usr" ..d, d)
		if ok == nil then
			print("FAILED to recreate " .. d .. " as link. Now we're in deep shit, sorry :-/")
		end
	end
end
