#
# spec file for package vlang
#
# Copyright (c) 2024, 2025 Boian Berberov
# Copyright (c) 2025 Eyad Issa
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

# git revision
%global vc_gitrev  048a0a537560080eb73d56e2f3b644462fa9037a

# custom paths and variables
%global vflags      -cc gcc -d dynamic_boehm
%global vexe_root   %{_libexecdir}/%{name}
%global vexe        %{vexe_root}/%{name}

Name:           vlang
Version:        0.4.12
Release:        0
Summary:        The V Programming Language
License:        MIT AND BSD-2-Clause
URL:            https://vlang.io/
Source0:        https://github.com/%{name}/v/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{name}/vc/raw/%{vc_gitrev}/v.c
Source99:       vlang-rpmlintrc
Patch0:         https://github.com/vlang/v/pull/25370.diff#/fix-already-unsafe.patch
BuildRequires:  c_compiler
BuildRequires:  diffutils
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  pkgconfig
# For VFLAGS="-d dynamic_boehm"
BuildRequires:  pkgconfig(bdw-gc)
# For vshare tool
BuildRequires:  pkgconfig(x11)
# For VFLAGS="-d dynamic_boehm"
# Required by compiler at runtime
Requires:       pkgconfig(bdw-gc)

%description
V is a statically typed compiled programming language inspired
by Go but with a more low-level approach, similar to C or Rust.

%package examples
Summary:        Examples for the V Programming Language
BuildArch:      noarch

%description examples
V is a statically typed compiled programming language inspired
by Go but with a more low-level approach, similar to C or Rust.

This package contains examples for the V Programming Language.

%prep
%autosetup -n v-%{version} -p1

# Remove .gitignore files
find . -type f -name '.gitignore' -print -delete

# Replace hardcoded path to v in examples
sed -i -e '1s:%{_prefix}/local/bin/v:%{_bindir}/%{name}:' examples/v_script.vsh

%build
export CC=cc
export CFLAGS="${CFLAGS} -std=gnu11 -pthread -w"

# Distro specific build flags
%{set_build_flags}

export VFLAGS="%{vflags}"

%if 0%{?sle_version} == 150500
export STAGE0_FLAGS='-lm -lpthread -lrt'
%else
export STAGE0_FLAGS='-lm -lpthread'
%endif

export STAGE1_FLAGS='-no-parallel'
%ifarch x86_64 %{ix86}
export STAGE2_FLAGS='-prod -nocache'
%else
export STAGE2_FLAGS='-nocache'
%endif

# stage 0: build the V compiler from the transpiled C code
${CC} ${CFLAGS} ${LDFLAGS} ${STAGE0_FLAGS} -o %{name}-stage0 %{SOURCE1}
# stage 1: build without parallelism
./%{name}-stage0 ${VFLAGS} ${STAGE1_FLAGS} -o %{name}-stage1 cmd/v
# stage 2: build with parallelism and -prod
./%{name}-stage1 ${VFLAGS} ${STAGE2_FLAGS} -o %{name}-stage2 cmd/v

# stage 3: rebuild and check diff
./%{name}-stage2 ${VFLAGS} ${STAGE2_FLAGS} -o %{name} cmd/v

diff --strip-trailing-cr -u %{name}-stage2 %{name}
if [ $? -eq 0 ]; then
  echo "Stage 3 build differs from the final build, please check the output above."
fi

# Replace some tools with dummy scripts
echo "println('\"%{name} up\" is disabled for the packaged versions of V')"   >  cmd/tools/vup.v
echo "println('Use your package manager to update V')"                        >> cmd/tools/vup.v
echo "println('\"%{name} self\" is disabled for the packaged versions of V')" >  cmd/tools/vself.v
echo "println('Use your package manager to update V')"                        >> cmd/tools/vself.v

# TODO: Skipping building vdoc until https://github.com/vlang/markdown is embedded in build
sed -i -e "/^const tools_in_subfolders/s/ 'vdoc',//" cmd/tools/vbuild-tools.v
rm -rf cmd/tools/vdoc

# Set to not-empty to skip build-time V module cloning with `git`
export VTEST_SANDBOXED_PACKAGING='yes'

# Build-time configuration
export VEXE="%{_builddir}/%{buildsubdir}/%{name}"
export VMODULES="%{_builddir}/%{buildsubdir}/.vmodules"
export VJOBS="%{?jobs:%jobs}"

# Print information about the build
./%{name} doctor

# Build V tools
# ./%%{name} test-self
./%{name} -v build-tools

# Do not attempt to rebuild after installation
echo 'disable' > cmd/tools/.disable_autorecompilation
chmod 0444    cmd/tools/.disable_autorecompilation

%install

# Remove development files
rm -rf \
	cmd/tools/*/tests \
	cmd/tools/fuzz \
	cmd/tools/vpm/expect \
	cmd/tools/install_wabt.vsh \
	cmd/tools/*/testdata \
	cmd/tools/install_binaryen.vsh \
	cmd/tools/git_pre_commit_hook.vsh \
	cmd/tools/bench/map_clear_runner.vsh \
	cmd/tools/check_retry.vsh

# Remove test files
rm -rf \
	vlib/*/tests \
	vlib/*/*/tests \
	vlib/*/*/*/tests \
	vlib/*/slow_tests \
	vlib/*/testdata \
	vlib/*/*/testdata \
	vlib/*/*/*/testdata \
	vlib/v/pkgconfig/test_samples \
	vlib/net/http/mime/build.vsh \

# Copy files
install -D -m 0755 %{name} %{buildroot}%{vexe}
cp -R                   -t %{buildroot}%{vexe_root} cmd vlib

# Install third-party headers
install -d %{buildroot}%{vexe_root}/thirdparty
cp -R -t %{buildroot}%{vexe_root}/thirdparty \
    thirdparty/stdatomic \
    %{nil}

# Run-time configuration wrapper
# TODO: Add a proper VTMP
install -d %{buildroot}%{_bindir}
echo '#! %{_bindir}/sh
export VEXE="%{vexe}"
export VCACHE="${HOME}/.cache/%{name}"
export VFLAGS="%{vflags}"

exec ${VEXE} $@
' > %{buildroot}%{_bindir}/%{name}
chmod 755 %{buildroot}%{_bindir}/%{name}

# symlink /usr/bin/vlang to /usr/bin/v
ln -rs %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/v

# Remove executable bits from examples
find examples -type f -exec chmod 0644 {} \;
# Copy examples
install -d %{buildroot}%{_datadir}/doc/%{name}/
cp -R -t %{buildroot}%{_datadir}/doc/%{name}/ examples

# Create shell completion files
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
%{buildroot}%{vexe} complete setup bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
sed -i 's|%{buildroot}||g' %{buildroot}%{_datadir}/bash-completion/completions/%{name}

mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
%{buildroot}%{vexe} complete setup zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
sed -i 's|%{buildroot}||g' %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{vexe} complete setup fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
sed -i 's|%{buildroot}||g' %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

# Remove duplicate files
%fdupes %{buildroot}%{_libexecdir}/%{name}/
%fdupes %{buildroot}%{_datadir}/doc/%{name}/examples

# %%check
# %%{name} test-self


%files
%license LICENSE
%doc CHANGELOG.md README.md
%doc doc/docs.md doc/vscode.md doc/img tutorials
%{_bindir}/v
%{_bindir}/%{name}
%{_libexecdir}/%{name}
# bash completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
# zsh completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
# fish completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files examples
%dir %{_datadir}/doc/%{name}/
%{_datadir}/doc/%{name}/examples

%changelog
