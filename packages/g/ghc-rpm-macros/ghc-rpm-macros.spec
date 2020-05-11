#
# spec file for package ghc-rpm-macros
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global macros_dir %{_sysconfdir}/rpm
%global without_hscolour 1
Name:           ghc-rpm-macros
Version:        1.9.95
Release:        0
Summary:        RPM Macros for building packages for GHC
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
Url:            https://fedoraproject.org/wiki/Haskell_SIG
# source gets updated with osc service dr
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  xz
Requires:       rpm
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

%package -n ghc-srpm-macros
Summary:        RPM macros for building Haskell source packages
Group:          Development/Libraries/Other
BuildArch:      noarch

%description -n ghc-srpm-macros
Macros used when generating source Haskell rpm packages.

%prep
%setup -q

%build
echo no build stage needed

%install
install -p -D -m 0644 macros.ghc %{buildroot}%{macros_dir}/macros.ghc
install -p -D -m 0644 macros.ghc-extra %{buildroot}/%{macros_dir}/macros.ghc-extra
install -p -D -m 0644 macros.ghc-suse %{buildroot}/%{macros_dir}/macros.ghc-suse
install -p -D -m 0755 ghc-deps.sh %{buildroot}/%{_prefix}/lib/rpm/ghc-deps.sh
install -p -D -m 0755 cabal-tweak-dep-ver %{buildroot}/%{_bindir}/cabal-tweak-dep-ver
install -p -D -m 0755 cabal-tweak-drop-dep %{buildroot}/%{_bindir}/cabal-tweak-drop-dep
install -p -D -m 0755 cabal-tweak-flag %{buildroot}/%{_bindir}/cabal-tweak-flag
install -p -D -m 0755 ghc-pkg-wrapper %{buildroot}/%{_prefix}/lib/rpm/ghc-pkg-wrapper
install -p -D -m 0644 ghc.attr %{buildroot}/%{_prefix}/lib/rpm/fileattrs/ghc.attr
install -p -D -m 0755 ghc-dirs.sh %{buildroot}/%{_prefix}/lib/rpm/ghc-dirs.sh
install -p -D -m 0644 Setup.hs %{buildroot}/%{_datadir}/%{name}/Setup.hs

%files
%doc AUTHORS
%license COPYING
%config %{macros_dir}/macros.ghc
%config %{macros_dir}/macros.ghc-suse
%{_prefix}/lib/rpm/ghc-deps.sh
%{_bindir}/cabal-tweak-dep-ver
%{_bindir}/cabal-tweak-flag
%{_bindir}/cabal-tweak-drop-dep
%{_prefix}/lib/rpm/ghc-pkg-wrapper
%{_prefix}/lib/rpm/fileattrs/ghc.attr
%{_prefix}/lib/rpm/ghc-dirs.sh
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/Setup.hs

%files extra
%config %{macros_dir}/macros.ghc-extra

%changelog
