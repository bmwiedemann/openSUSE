#
# spec file for package qbe
#
# Copyright (c) 2023 SUSE LLC
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


Name:           qbe
Version:        1.0
Release:        0
Summary:        Small embeddable C compiler backend
Group:          Development/Languages/Other
URL:            https://c9x.me/compile
Source0:        https://c9x.me/compile/release/qbe-%{version}.tar.xz
License:        MIT

%description
QBE is a compiler backend that aims to provide 70% of the
performance of industrial optimizing compilers in 10% of the code.
QBE fosters language innovation by offering a compact user-friendly
and performant backend.

The size limit constrains QBE to focus on the essential and
prevents embarking on a never-ending path of diminishing returns.

%prep
%setup -q

%build
export CC="cc"
%make_build CFLAGS="%optflags -std=c99 -fPIE"

%install
%make_install PREFIX="%_prefix"

%files
%{_bindir}/%{name}
%license LICENSE
%doc README doc

%changelog
