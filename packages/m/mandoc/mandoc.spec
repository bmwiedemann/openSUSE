#
# spec file for package mandoc
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.14.6
Release:        0
%define nvr %{name}-%{version}-%{release}
Summary:        UNIX manpage compiler
License:        ISC
Group:          Productivity/Publishing/Troff
URL:            http://mandoc.bsd.lv/
Source:         http://mandoc.bsd.lv/snapshots/mandoc-%{version}.tar.gz
BuildRequires:  less
BuildRequires:  zlib-devel
Requires:       %{name}-bin = %{version}
Provides:       man = %{version}
Conflicts:      groff
Conflicts:      groff-full
Conflicts:      makewhat
Conflicts:      man
# file triggers use rpm.execute()
Conflicts:      rpm < 4.15

%description
The mandoc manpage compiler toolset (formerly called "mdocml")
is a suite of tools compiling mdoc(7), the roff(7) macro language
of choice for BSD manual pages, and man(7), the predominant
historical language for UNIX manuals.

It includes a man(1) manual viewer and additional tools.
For general information, see <http://mandoc.bsd.lv/>.

%package bin
Summary:        Format manual pages

%description bin
The mandoc utility formats manual pages for display.

It is split out from the mandoc package as it can be useful
even without replacing the entire man infrastructure.

%prep
%autosetup -p1

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
-- no point registering individual files if we can call
-- makewhatis in %%post to catch all if
if posix.getenv("VERBOSE_FILETRIGGERS") then
    print("%{nvr}: running file install trigger")
end
if posix.access("%{_mandir}/mandoc.db") then
    file = rpm.next_file()
    while file do
        if string.match(file, "%{_mandir}/man[^/]+/[^/]+%{?ext_man}$") then
            if posix.access(file) then
                if posix.getenv("VERBOSE_FILETRIGGERS") then
                    print("%{nvr}: adding " .. file)
                end
                rpm.execute("%{_sbindir}/makewhatis", "-d", "%{_mandir}", file)
            else
                io.stderr:write("%{nvr}: missing " .. file .. "\n")
            end
        end
        file = rpm.next_file()
    end
elseif posix.getenv("VERBOSE_FILETRIGGERS") then
    print("%{nvr}: missing mandoc.db, skipped")
end
io.flush()

%filetriggerun -p <lua> -- %{_mandir}
if posix.getenv("VERBOSE_FILETRIGGERS") then
    print("%{nvr}: running file remove trigger")
end
if posix.access("%{_mandir}/mandoc.db") then
    file = rpm.next_file()
    while file do
        if string.match(file, "%{_mandir}/man[^/]+/[^/]+%{?ext_man}$") then
            if posix.access(file) then
                if posix.getenv("VERBOSE_FILETRIGGERS") then
                    print("%{nvr}: removing " .. file)
                end
                rpm.execute("%{_sbindir}/makewhatis", "-u", "%{_mandir}", file)
            else
                io.stderr:write("%{nvr}: missing " .. file .. "\n")
            end
        end
        file = rpm.next_file()
    end
elseif posix.getenv("VERBOSE_FILETRIGGERS") then
    print("%{nvr}: missing mandoc.db, skipped")
end
io.flush()

%files
%license LICENSE
%doc NEWS TODO
%{_bindir}/apropos
%{_bindir}/demandoc
%{_bindir}/man
%{_bindir}/soelim
%{_bindir}/whatis
%{_sbindir}/makewhatis
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%{_mandir}/man7/*.7%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}
%ghost %{_mandir}/mandoc.db

%files bin
%{_bindir}/mandoc

%changelog
