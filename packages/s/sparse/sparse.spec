#
# spec file for package sparse
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


%bcond_with llvm

Name:           sparse
Version:        0.6.4+20220627
Release:        0
Summary:        A semantic parser of source files
License:        MIT
Group:          Development/Tools/Building
URL:            https://sparse.docs.kernel.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
%if %{with llvm}
%ifarch         x86_64
BuildRequires:  clang
BuildRequires:  llvm-devel < 16
%endif
%endif

%description
Sparse is a semantic parser of source files: it's neither a compiler
(although it could be used as a front-end for one) nor is it a
preprocessor (although it contains as a part of it a preprocessing
phase).

It is meant to be a small - and simple - library.  Scanty and meager,
and partly because of that easy to use.  It has one mission in life:
create a semantic parse tree for some arbitrary user for further
analysis.  It's not a tokenizer, nor is it some generic context-free
parser.  In fact, context (semantics) is what it's all about - figuring
out not just what the grouping of tokens are, but what the _types_ are
that the grouping implies.

Sparse is primarily used in the development and debugging of the Linux
kernel.

%package inspect
Summary:        Inspect binary from sparse
Group:          Development/Libraries/C and C++

%description inspect
test-inspect is a gtk frontend for sparse.

%if %{with llvm}
%package llvm
Summary:        LLVM backed sparse
Group:          Development/Libraries/C and C++

%description llvm
LLVM backend for sparse, including sparsec
%endif

%prep
%autosetup -p1

%build
%make_build \
  PREFIX=%{_prefix} \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{optflags}" \
  V=1

%install
%make_install \
  PREFIX=%{_prefix}

%files
%license LICENSE
%doc README FAQ
%{_bindir}/cgcc
%{_bindir}/c2xml
%{_bindir}/semind
%{_bindir}/sparse
%{_mandir}/man1/cgcc.1%{?ext_man}
%{_mandir}/man1/semind.1%{?ext_man}
%{_mandir}/man1/sparse.1%{?ext_man}

%if %{with llvm}
%ifarch x86_64
%files llvm
%{_bindir}/sparsec
%{_bindir}/sparse-llvm
%endif
%endif

%files inspect
%{_bindir}/test-inspect

%changelog
