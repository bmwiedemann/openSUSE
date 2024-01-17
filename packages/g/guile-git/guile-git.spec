#
# spec file for package guile-git
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


Name:           guile-git
Version:        0.5.2
Release:        0
Summary:        Guile bindings of libgit2
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://gitlab.com/guile-git/guile-git
Source0:        https://gitlab.com/guile-git/guile-git/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-bytestructures
BuildRequires:  guile-devel
BuildRequires:  libgit2-devel
BuildRequires:  pkg-config
BuildRequires:  texinfo
Requires:       guile
Requires:       guile-bytestructures
Requires:       libgit2-devel
Requires(pre):  %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides Guile bindings to libgit2,
a library manipulate repositories of the Git version control system.

%prep
%setup -q -n %{name}-v%{version}
autoreconf -vif

%build
%configure
# build non-parallel for reproducible build results (boo#1170378)
make

%install
%make_install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/guile-git.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/guile-git.info.gz

%files
%defattr(-,root,root)
%license COPYING
%doc NEWS README.md
%{_libdir}/guile/*/site-ccache/git*
%{_datadir}/guile/site/*/git*
%{_infodir}/guile-git.info.gz

%changelog
