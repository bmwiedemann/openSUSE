#
# spec file for package colormake
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           colormake
Version:        0.9.20140503
Release:        0
Summary:        Colorize the make output
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            http://github.com/pagekite/Colormake
Source:         http://github.com/pagekite/Colormake/archive/%{version}.tar.gz
Patch0:         %{name}-clang.patch
Patch1:         %{name}-tests.patch
Patch2:         %{name}-gpp.patch
Patch3:         %{name}-silent-rules.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}

%description
A simple wrapper for making the output from make easier to read
(more colorful), and errors easier to find in messy compilations.
It was inspired by Micheal T. Babcock's excellent logcolorize program.

%prep
%setup -q -n Colormake-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i -e 's# make # %{_bindir}/make #g' \
    -e 's#colormake.pl#%{perl_vendorlib}/colormake.pl#g' colormake

%build

%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm0755 %{name}.pl %{buildroot}%{perl_vendorlib}/%{name}.pl
cp -a %{name}-short clmake* %{buildroot}%{_bindir}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING AUTHORS BUGS
%{_bindir}/%{name}*
%{_bindir}/clmake*
%{perl_vendorlib}/%{name}.pl
%{_mandir}/man1/%{name}.1.gz

%changelog
