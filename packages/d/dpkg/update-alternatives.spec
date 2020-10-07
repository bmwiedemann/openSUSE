#
# spec file for package update-alternatives
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


Name:           update-alternatives
Version:        1.19.0.5
Release:        0
Summary:        Maintain symbolic links determining default commands
License:        GPL-2.0-or-later
Group:          System/Management
URL:            http://ftp.de.debian.org/debian/pool/main/d/dpkg/
Source0:        http://ftp.de.debian.org/debian/pool/main/d/dpkg/dpkg_%{version}.tar.xz
Source3:        sensible-editor
Patch0:         update-alternatives-suse.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
Provides:       alternatives = %{version}

%description
update-alternatives creates, removes, maintains and displays
information about the symbolic links comprising the alternatives
system. It is possible for several programs fulfilling the same or
similar functions to be installed on a single system at the same time.
For example, many systems have several text editors installed at once.
This gives choice to the users of a system, allowing each to use a
different editor, if desired, but makes it difficult for a program to
make a good choice of editor to invoke if the user has not specified a
particular preference.

%prep
%setup -q -n dpkg-%{version}
%patch0 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf -fvi
%configure \
  --disable-silent-rules \
  --with-admindir=%{_localstatedir}/lib

make -C lib/compat %{?_smp_mflags}
make -C utils/ %{?_smp_mflags}
make -C man/ %{?_smp_mflags}

%install
install -d -m 0755 %{buildroot}/%{_sbindir}/
install -d -m 0755 %{buildroot}/%{_mandir}/man1/
install -d -m 0755 %{buildroot}/%{_sysconfdir}/alternatives
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/alternatives
install -d -m 0755 %{buildroot}/%{_localstatedir}/log

install -pm 0755 utils/%{name} %{buildroot}/%{_sbindir}
ln -s %{name} %{buildroot}/%{_sbindir}/alternatives
install -pm 0644 man/%{name}.1 %{buildroot}/%{_mandir}/man1/

%post -p <lua>
-- Migrate to new location
if posix.access('var/lib/rpm/alternatives', 'x') then
  print("migrating update alternatives database to new location")
  -- We proceed even if no alternatives directory exists, such situation
  -- occurs in buildroot environment
  new_location='%{_localstatedir}/lib/alternatives/'
  for i,old_file in pairs(posix.dir("var/lib/rpm/alternatives/")) do
    print(old_file.."\n")
    new_file = string.gsub(old_file, "(.*/)(.*)", new_location .. "%2")
    print(new_file.."\n")
    os.rename(old_file, new_file)
  end
  posix.rmdir('var/lib/rpm/alternatives')
end
-- touch file
io.open('%{_localstatedir}/log/alternatives.log', "w"):close()

%files
%license COPYING
%dir %{_sysconfdir}/alternatives
%dir %{_localstatedir}/lib/alternatives
%{_sbindir}/alternatives
%{_sbindir}/update-alternatives
%{_mandir}/man1/update-alternatives.1%{ext_man}
%ghost %{_localstatedir}/log/alternatives.log

%changelog
