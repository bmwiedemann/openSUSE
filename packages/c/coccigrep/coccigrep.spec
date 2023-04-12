#
# spec file for package coccigrep
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


Name:           coccigrep
Version:        1.20
Release:        0
Summary:        Semantic grep tool for C, based on coccinelle
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/regit/coccigrep
Source:         https://github.com/regit/coccigrep/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  xz
Requires:       coccinelle
Requires:       python3
# Mimicing coccinelle
ExclusiveArch:  aarch64 ppc64le powerpc64le s390x x86_64 riscv64
BuildArch:      noarch

%description
coccigrep is a semantic grep for the C language based on coccinelle. It can be
used to find where a given structure is used in code files. coccigrep depends on
the spatch program which comes with coccinelle.

%prep
%setup -q
chmod 644 README.rst

%build
%python3_build

%install
%python3_install

install -d %{buildroot}/%{_mandir}/man1/
install -m 644 coccigrep.1 %{buildroot}/%{_mandir}/man1/

%files
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/*
%{_bindir}/coccigrep
%{_mandir}/man1/coccigrep.1%{?ext_man}

%changelog
