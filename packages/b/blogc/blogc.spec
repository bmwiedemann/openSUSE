#
# spec file for package blogc
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


Name:           blogc
Version:        0.20.0
Release:        0
Summary:        Blog compiler
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Utilities
URL:            https://blogc.rgm.io/
Source:         https://github.com/blogc/blogc/releases/download/v%{version}/blogc-%{version}.tar.xz
BuildRequires:  xz

%description
blogc is a blog compiler. It converts source files and templates into blog/website resources.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/blogc
%{_mandir}/man1/blogc.1%{ext_man}
%{_mandir}/man7/blogc-pagination.7%{ext_man}
%{_mandir}/man7/blogc-source.7%{ext_man}
%{_mandir}/man7/blogc-template.7%{ext_man}
%{_mandir}/man7/blogc-toctree.7%{ext_man}

%changelog
