#
# spec file for package jp2a
#
# Copyright (c) 2024 SUSE LLC
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


%{!?license: %global license %doc}
Name:           jp2a
Version:        1.3.2
Release:        0
Summary:        Converts JPEG images to ASCII
License:        GPL-2.0-only
Group:          Amusements/Toys/Graphics
URL:            https://github.com/Talinx/jp2a
Source:         https://github.com/Talinx/jp2a/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libcurl-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  libpng-devel
BuildRequires:  libwebp-devel
BuildRequires:  unzip

%package bash-completion
Summary:        Bash completions scripts for jp2a
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%package zsh-completion
Summary:        Zsh completions scripts for jp2a
Supplements:    (%{name} and zsh-completion)
BuildArch:      noarch

%description
jp2a is a JPEG to ASCII converter.

%description bash-completion
This package contains the bash completions scripts for jp2a.

%description zsh-completion
This package contains the zsh completions scripts for jp2a.

%prep
%setup -q

%build
autoreconf -vi
%configure --enable-curl
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
mv %{buildroot}%{_sysconfdir}/bash_completion.d/jp2a %{buildroot}%{_datadir}/bash-completion/completions/

%check
pushd tests
make %{?_smp_mflags} check
popd

%files
%doc ChangeLog README NEWS
%license COPYING
%{_bindir}/jp2a
%{_mandir}/man1/jp2a.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/jp2a

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_jp2a

%changelog
