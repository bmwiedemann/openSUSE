#!/usr/bin/lua

-- test stubs
_test_name = string.gsub(arg[0], ".*/(.*)%.lua$", "%1")
function _progress(...)
    io.stdout:write(_test_name, ": ", ...)
end

function _add_buildroot(buildroot, var)
    local path_sep = package.config:sub(3,3);
    local path_sep_mask = path_sep:gsub('[()%%.[^$%]*+%-?]','%%%1')
    local mask = "([^" .. path_sep_mask .."]+)"

    local paths = {}
    for p in var:gmatch(mask) do
        if not (p:sub(1, 2) == './') then
            table.insert(paths, buildroot .. p)
        end
        table.insert(paths, p)
    end
    return table.concat(paths, path_sep)
end

if arg[1] then
    local buildroot = arg[1]
    _progress("add buildroot ", buildroot, " to package.path - ")
    package.path = _add_buildroot(buildroot, package.path)
    print("done")

    _progress("add buildroot ", buildroot, " to package.cpath - ")
    package.cpath = _add_buildroot(buildroot, package.cpath)
    print("done")
end
-- /test stubs

_progress("--- Test modules loading from:\n")
_progress("package.path=")
print(package.path)
_progress("package.cpath=")
print(package.cpath)
_progress("---\n")

-- run test
local modules = {
    { 'lua',  'DBI' },
    { 'MySQL', 'dbd.mysql' },
    { 'PostgreSQL', 'dbd.postgresql' },
    { 'SQLite3', 'dbd.sqlite3' },
}

errors = 0
for _, m in ipairs(modules) do
    driver = m[1]
    modulefile = m[2]

    _progress("load ", driver, " module ", modulefile, ": ")
    local m, err = pcall(require, modulefile)
    if m then
        print("success");
    else
        print("FAILED, err="..err);
        print()
        errors = errors + 1;
    end
end

_progress()
if errors == 0 then
    print("SUCCESS")
    os.exit(0)
else
    print("FAILED, " .. errors .. " error(s) found")
    os.exit(1)
end
