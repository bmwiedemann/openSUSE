#
# spec file for package roast
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           roast
Version:        10.0.2
Release:        0
Summary:        Simpler tar archiver and extractor
License:        MPL-2.0
URL:            https://github.com/openSUSE-Rust/roast
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)

%package -n obs-service-recomprizz
Summary:        OBS Source Service for recomprizz-ion
License:        MPL-2.0

%description -n obs-service-recomprizz
Utility to recompress to other compression formats.

%package -n obs-service-roast
Summary:        OBS Source Service for roast
License:        MPL-2.0

%description -n obs-service-roast
Utility to roast source directories into highly compressed tape archives.

%package -n obs-service-raw
Summary:        OBS Source Service for raw
License:        MPL-2.0

%description -n obs-service-raw
Utility to raw decompress tape archives to unarchived sources.

%package -n obs-service-roast_scm
Summary:        OBS Source Service for roast_scm
License:        MPL-2.0

%description -n obs-service-roast_scm
Utility to roast remote git repositories as tarball sources.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       %{name}
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       %{name}
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       %{name}
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%description
Roast is a simple tar archiver and extractor with very high
compression settings for supported formats such as zstd.

It also supports recompression from an existing tarball.

%prep
%autosetup -a1

%build
%{cargo_build} -p roast-cli --bins -F obs --target-dir %{_builddir}/%{buildsubdir}/target
mkdir with_feature_obs/
cp %{_builddir}/%{buildsubdir}/target/release/roast with_feature_obs/
cp %{_builddir}/%{buildsubdir}/target/release/roast_scm with_feature_obs/
cp %{_builddir}/%{buildsubdir}/target/release/raw with_feature_obs/
cp %{_builddir}/%{buildsubdir}/target/release/recomprizz with_feature_obs/
# Build again for no obs feature. Those will be installed in %{_bindir}
%{cargo_build} -p roast-cli --bins --target-dir %{_builddir}/%{buildsubdir}/target

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
pushd roast-cli
%{cargo_install} --bins --target-dir %{_builddir}/%{buildsubdir}/target
popd
cp -v %{_builddir}/%{buildsubdir}/with_feature_obs/roast %{buildroot}%{_prefix}/lib/obs/service/roast
install -m0644 roast.service %{buildroot}%{_prefix}/lib/obs/service
cp -v %{_builddir}/%{buildsubdir}/with_feature_obs/recomprizz %{buildroot}%{_prefix}/lib/obs/service/recomprizz
install -m0644 recomprizz.service %{buildroot}%{_prefix}/lib/obs/service
cp -v %{_builddir}/%{buildsubdir}/with_feature_obs/raw %{buildroot}%{_prefix}/lib/obs/service/raw
install -m0644 raw.service %{buildroot}%{_prefix}/lib/obs/service
cp -v %{_builddir}/%{buildsubdir}/with_feature_obs/roast_scm %{buildroot}%{_prefix}/lib/obs/service/roast_scm
install -m0644 roast_scm.service %{buildroot}%{_prefix}/lib/obs/service

# Removes the Roast SCM binary with underscore name in /usr/bin
rm %{buildroot}/%{_bindir}/roast_scm

export PATH="${PATH:-}:%{buildroot}/%{_bindir}"
for roast_command in "roast-scm" "roast" "recomprizz" "raw"
do
  for shell in "zsh" "bash" "fish"
  do
    if [ "$shell" = "bash" ]
    then
          mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
    	$roast_command generate-completions-for "$shell" > %{buildroot}%{_datadir}/bash-completion/completions/${roast_command}.bash
    fi
    if [ "$shell" = "zsh" ]
    then
          mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
    	$roast_command generate-completions-for "$shell" > %{buildroot}%{_datadir}/zsh/site-functions/_${roast_command}
    fi
    if [ "$shell" = "fish" ]
    then
          mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d/
    	$roast_command generate-completions-for "$shell" > %{buildroot}%{_datadir}/fish/vendor_completions.d/${roast_command}.fish
    fi
  done
done

%check
%{cargo_test} --test repro --target-dir %{_builddir}/%{buildsubdir}/target
%{cargo_test} --test shame --target-dir %{_builddir}/%{buildsubdir}/target

%files
%{_bindir}/roast
%{_bindir}/raw
%{_bindir}/recomprizz
%{_bindir}/roast-scm
%license LICENCE
%doc     CHANGELOG.md README.md

%files -n obs-service-roast
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/roast
%{_prefix}/lib/obs/service/roast.service
%license LICENCE
%doc     CHANGELOG.md README.md

%files -n obs-service-recomprizz
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/recomprizz
%{_prefix}/lib/obs/service/recomprizz.service
%license LICENCE
%doc     CHANGELOG.md README.md

%files -n obs-service-raw
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/raw
%{_prefix}/lib/obs/service/raw.service
%license LICENCE
%doc     CHANGELOG.md README.md

%files -n obs-service-roast_scm
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/roast_scm
%{_prefix}/lib/obs/service/roast_scm.service
%license LICENCE
%doc     CHANGELOG.md README.md

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/*

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/*

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/*

%changelog
