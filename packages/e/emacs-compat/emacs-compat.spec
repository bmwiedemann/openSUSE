#
# spec file for package emacs-compat
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Björn Bidar
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


%global _name    compat

Name:           emacs-%{_name}
Version:        29.1.4.4
Release:        0
Summary:        COMPATibility Library for Emacs Lisp
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://github.com/emacs-compat/compat
Source0:        %{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  emacs-nox
BuildRequires:  info
BuildRequires:  make
BuildRequires:  makeinfo
Requires:       emacs
Supplements:    emacs
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
# PATCH-FEATURE-UPSTREAM install targets PR 30
Patch1:         0001-Add-install-target.patch

%description
compat.el, the forwards-compatibility library for (GNU) Emacs Lisp, versions 24.4 and newer. The intended audience are package developers that are interested in using newer developments, without having to break compatibility.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%make_build

%install
%make_install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{_name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{_name}.info.gz

%files
%doc README.md
%license COPYING
%{_emacs_sitelispdir}/%{_name}*.el*
%{_infodir}/%{_name}*

%changelog
