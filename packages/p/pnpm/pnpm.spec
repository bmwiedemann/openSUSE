#
# spec file for package pnpm
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


# to avoid empty debugfiles error on some distros
%global debug_package %{nil}
# The internal dependency generator adds lots of unnecessary Requires:
# and strange Provides: own(foo) because it slurps in all package.json
%global __nodejs_provides %{nil}
%global __nodejs_requires %{nil}
Name:           pnpm
Version:        9.13.2
Release:        0
Summary:        Fast, disk space efficient package manager
License:        MIT
Group:          Development/Languages/Other
URL:            https://pnpm.io/
Source:         https://registry.npmjs.org/%{name}/-/%{name}-%{version}.tgz
BuildRequires:  fdupes
BuildRequires:  nodejs-devel >= 18
BuildRequires:  nodejs-packaging
Requires:       bash
Recommends:     python3
Provides:       npm(%{name}) = %{version}
BuildArch:      noarch

%description
pnpm is a package manager for node.js

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       fish
Supplements:    (%{name} and fish)

%description fish-completion
Fish command line completion support for %{name}.

%prep
%setup -q -n package

%build
# nothing to do

%install
%nodejs_install

# PATCH FILES

fix_executable() { chmod 775 "$1"; sed -i '1 s|^\(#!.*/\)env |\1|' "$1"; }
export -f fix_executable

# Patch hashbang in pnpm
sed -i -e 's|#!%{_bindir}/env node|#!%{_bindir}/node|' %{buildroot}%{nodejs_sitelib}/pnpm/bin/*

sed -i '1 s|^\(#!.*/\)env |\1|' %{buildroot}%{nodejs_sitelib}/pnpm/dist/node-gyp-bin/node-gyp

# Non-executable scripts
find %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules -type f -path '*/bin/*' \
    -exec sh -c 'fix_executable {}' \;
fix_executable %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules/glob/dist/esm/bin.mjs

# Remove unnecessary shebangs
sed -i '1!b;\|#!/|d' %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules/glob/dist/esm/bin.d.mts
find %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules/node-gyp/gyp -type f \
    -exec sed -i '1!b;\|#!/|d' {} \;

# SHELL COMPLETION

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
%{buildroot}%{_bindir}/pnpm completion bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
%{buildroot}%{_bindir}/pnpm completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{_bindir}/pnpm completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

# CLEANUP

# Hidden files
find %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules -type f -name '.*' -delete

# Hidden directories
find %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules -type d -name '.*' -print0 | xargs -0 -n1 rm -rvf

# Non-Linux files
rm -rf %{buildroot}%{nodejs_sitelib}/pnpm/dist/vendor
rm -f %{buildroot}%{nodejs_sitelib}/pnpm/dist/reflink.{darwin,win32}*.node
rm -f %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules/node-gyp/macOS_*
find %{buildroot}%{nodejs_sitelib}/pnpm/dist -type f \
    \( -name '*.cmd' -o -name '*.bat' -o -name '*.ps1' \) -delete

%fdupes %{buildroot}

%check

%files
%license LICENSE
%doc README.md
%{_bindir}/pnp{m,x}
%{nodejs_sitelib}

%files bash-completion
%{_datadir}/bash-completion/

%files zsh-completion
%{_datadir}/zsh/

%files fish-completion
%{_datadir}/fish/

%changelog
