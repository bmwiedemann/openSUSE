#
# spec file for package ghc-rpm-macros
#
# Copyright (c) 2021 SUSE LLC
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


%global without_hscolour 1
Name:           ghc-rpm-macros
Version:        2.5.2
Release:        0
Summary:        RPM Macros for building packages for GHC
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://fedoraproject.org/wiki/Haskell_SIG
# source gets updated with osc service dr
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  xz
Requires:       rpm
Requires:       chrpath
BuildArch:      noarch
%if %{undefined without_hscolour}
Requires:       hscolour
%endif

%description
A set of macros for building GHC packages following the openSUSE
Haskell Guidelines.  ghc needs to be installed in
order to make use of these macros.

%package extra
Summary:        Extra RPM macros for building Haskell packages with several libs
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}

%description extra
Extra macros used for subpackaging of Haskell libraries,
for example in ghc and haskell-platform.

%prep
%setup -q

%build
echo no build stage needed

%install
install -p -D -m 0644 macros.ghc %{buildroot}%{_rpmmacrodir}/macros.ghc
install -p -D -m 0644 macros.ghc-extra %{buildroot}/%{_rpmmacrodir}/macros.ghc-extra
install -p -D -m 0644 macros.ghc-suse %{buildroot}/%{_rpmmacrodir}/macros.ghc-suse
install -p -D -m 0755 ghc-deps.sh %{buildroot}/%{_prefix}/lib/rpm/ghc-deps.sh
install -p -D -m 0755 cabal-tweak-dep-ver %{buildroot}/%{_bindir}/cabal-tweak-dep-ver
install -p -D -m 0755 cabal-tweak-drop-dep %{buildroot}/%{_bindir}/cabal-tweak-drop-dep
install -p -D -m 0755 cabal-tweak-flag %{buildroot}/%{_bindir}/cabal-tweak-flag
install -p -D -m 0755 cabal-tweak-remove-upperbound %{buildroot}/%{_bindir}/cabal-tweak-remove-upperbound
install -p -D -m 0755 ghc-pkg-wrapper %{buildroot}/%{_prefix}/lib/rpm/ghc-pkg-wrapper
install -p -D -m 0644 ghc.attr %{buildroot}/%{_prefix}/lib/rpm/fileattrs/ghc.attr
install -p -D -m 0644 Setup.hs %{buildroot}/%{_datadir}/%{name}/Setup.hs

%files
%doc AUTHORS
%license COPYING
%{_rpmmacrodir}/macros.ghc
%{_rpmmacrodir}/macros.ghc-suse
%{_prefix}/lib/rpm/ghc-deps.sh
%{_bindir}/cabal-tweak-dep-ver
%{_bindir}/cabal-tweak-flag
%{_bindir}/cabal-tweak-drop-dep
%{_bindir}/cabal-tweak-remove-upperbound
%{_prefix}/lib/rpm/ghc-pkg-wrapper
%{_prefix}/lib/rpm/fileattrs/ghc.attr
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/Setup.hs

%files extra
%{_rpmmacrodir}/macros.ghc-extra

%changelog
