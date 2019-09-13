#
# spec file for package man-pages-fr
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Source file has sometimes a revision number (major.minor-revision).
# If not, replace by the nil macro
%define revision -1

Name:           man-pages-fr
Version:        3.70
Release:        0
Summary:        LDP man Pages (French)
License:        GPL-2.0 and GPL-2.0+ and BSD-3-Clause and GFDL-1.1 and GFDL-1.2
Group:          Documentation/Man
Url:            http://traduc.org/
Source:         http://perkamon.alioth.debian.org/archives/%{version}/man-pages-fr-%{version}%{revision}.tar.xz
Suggests:       man-pages-fr-extra
Provides:       locale(man-pages:fr)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
These are the French man pages of the Linux Documentation Project. Note
that they are normally older than the English versions. For reference,
you should use the English versions.

%prep
%setup -q -n fr

%build

%install
mkdir -p %{buildroot}%{_mandir}/fr
for section in man? ; do
  mkdir -p %{buildroot}%{_mandir}/fr/$section
  install -m 644 $section/* %{buildroot}%{_mandir}/fr/$section
done
%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%defattr(-,root,root)
%doc README.fr

%changelog
