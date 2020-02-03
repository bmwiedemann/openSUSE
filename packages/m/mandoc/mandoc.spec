#
# spec file for package mandoc
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           mandoc
Version:        1.14.5
Release:        0
Summary:        UNIX manpage compiler
License:        ISC
Group:          Productivity/Publishing/Troff
URL:            http://mandoc.bsd.lv/
Source:         http://mandoc.bsd.lv/snapshots/mandoc-%{version}.tar.gz
BuildRequires:  zlib-devel
Provides:       man = %{version}
Conflicts:      man
Conflicts:      groff
Conflicts:      groff-full
Conflicts:      makewhat

%description
The mandoc manpage compiler toolset (formerly called "mdocml")
is a suite of tools compiling mdoc(7), the roff(7) macro language
of choice for BSD manual pages, and man(7), the predominant
historical language for UNIX manuals.

It includes a man(1) manual viewer and additional tools.
For general information, see <http://mandoc.bsd.lv/>.

%prep
%setup -q

%build
%{?!make_build:%define make_build make %{?_smp_mflags} V=1 VERBOSE=1}
export CPPFLAGS="%{optflags}"
export CFLAGS="%optflags"
%configure
%make_build

%install
%make_install MANDIR=%{_mandir} BINDIR=%{_bindir} SBINDIR=%{_sbindir}
cp -fv %{buildroot}%{_bindir}/apropos %{_tmppath}/
mv -fv %{_tmppath}/apropos %{buildroot}%{_sbindir}/makewhatis

# ghost
: > %{buildroot}%{_mandir}/mandoc.db

%post
%{_sbindir}/makewhatis

%filetriggerin -p <lua> -- %{_mandir}
-- TODO: replace with rpm.execute after rpm 4.15
function execute(path, ...)
  local pid = posix.fork()
  if pid == 0 then
     posix.exec(path, ...)
     io.write(path, ": exec failed: ", posix.errno(), "\n")
     os.exit(1)
  end
  if not pid then
     error(path .. ": fork failed: " .. posix.errno() .. "\n")
  end
  posix.wait(pid)
end
--
-- no point registering individual files if we can call
-- makewhatis in %%post to catch all if
if posix.access("%{_mandir}/mandoc.db") then
    file = rpm.next_file()
    while file do
        if string.match(file, "%{_mandir}/man[^/]+/[^/]+%{?ext_man}$") then
            execute("%{_sbindir}/makewhatis", "-d", "%{_mandir}", file)
        end
        file = rpm.next_file()
    end
end

%filetriggerun -p <lua> -- %{_mandir}
-- TODO: replace with rpm.execute after rpm 4.15
function execute(path, ...)
  local pid = posix.fork()
  if pid == 0 then
     posix.exec(path, ...)
     io.write(path, ": exec failed: ", posix.errno(), "\n")
     os.exit(1)
  end
  if not pid then
     error(path .. ": fork failed: " .. posix.errno() .. "\n")
  end
  posix.wait(pid)
end
--
if posix.access("%{_mandir}/mandoc.db") then
    file = rpm.next_file()
    while file do
        if string.match(file, "%{_mandir}/man[^/]+/[^/]+%{?ext_man}$") then
            execute("%{_sbindir}/makewhatis", "-u", "%{_mandir}", file)
        end
        file = rpm.next_file()
    end
end

%files
%license LICENSE
%doc NEWS TODO
%{_bindir}/apropos
%{_bindir}/demandoc
%{_bindir}/man
%{_bindir}/mandoc
%{_bindir}/soelim
%{_bindir}/whatis
%{_sbindir}/makewhatis
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%{_mandir}/man7/*.7%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}
%ghost %{_mandir}/mandoc.db

%changelog
