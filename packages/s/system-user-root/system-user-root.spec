#
# spec file for package system-user-root
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           system-user-root
Version:        20190513
Release:        0
Summary:        System user and group root
License:        MIT
Group:          System/Fhs
Source1:        system-user-root.conf
BuildArch:      noarch
Provides:       group(root)
Provides:       group(shadow)
Provides:       group(trusted)
Provides:       group(users)
Provides:       user(root)
#!BuildIgnore: group(root)
#!BuildIgnore: group(trusted)
#!BuildIgnore: user(root)

%description
This package provides the root account including the groups root,
shadow and users.


%prep
%setup -q -c -T

%build

%install
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/system-user-root.conf

%pre -p <lua>
if not posix.access("/etc", "f") then
  posix.mkdir("/etc")
end
if not posix.access("/etc/passwd", "f") then
  file = io.open("/etc/passwd", "a+")
  file:write("root:x:0:0:root:/root:/bin/bash\n")
  file:close()
  posix.chmod("/etc/passwd", 0644)
end
if not posix.access("/etc/group", "f") then
  file = io.open("/etc/group", "a+")
  file:write("root:x:0:\nshadow:x:15:\ntrusted:x:42:\nusers:x:100:\n")
  file:close()
  posix.chmod("/etc/group", 0644)
end
if not posix.access("/etc/shadow", "f") then
  file = io.open("/etc/shadow", "a+")
  local date = os.time()
  date = math.floor(date / 86400)
  file:write("root:*:", date, "::::::\n")
  file:close()
  posix.chown("/etc/shadow", 0, 15)
  posix.chmod("/etc/shadow", 0640)
end

%files
%defattr(-,root,root)
%{_sysusersdir}/system-user-root.conf

%changelog
