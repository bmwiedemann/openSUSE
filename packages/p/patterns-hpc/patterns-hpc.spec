#
# spec file for package patterns-hpc
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


Name:           patterns-hpc
Version:        20190218
Release:        0
Summary:        Source Package for HPC Patterns
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
Source1:        library-inc.txt
Source2:        devel-inc.txt
BuildRequires:  patterns-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64 aarch64

%description
This is an internal package that is used to create the patterns as part of
the installation source setup.  Installation of this package does not make
sense.
This particular package contains all the HPC related patterns.





################################################################################
%package compute_node
%pattern_serverfunctions
Summary:        HPC Basic Compute Node
Group:          Metapackages
Provides:       pattern() = hpc_compute_node
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-visible()

Requires:       nfs-client
Requires:       openssh
Requires:       sudo
# Ping is useful on compute nodes (bsc#1169484)
Requires:       iputils

Recommends:     less
Recommends:     mrsh
Recommends:     mrsh-server
Recommends:     nss_ldap
Recommends:     ntp
Recommends:     pdsh
Recommends:     rsync
Recommends:     salt-minion
Recommends:     slurm-node
Recommends:     vim
Recommends:     wget
# python 2.7 deps
Recommends:     ganglia-gmond
Recommends:     genders
Recommends:     perl-genders

%description compute_node
A compute node comprises of a minimal software image and mainly runs simulation programs. Services on this node should be reduced to a bare minimum and the node *must* be installed in a automatic manner.
The pattern 'HPC Modularized libraries' should also be installed.

%files compute_node
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/patterns-hpc-compute_node.txt

################################################################################

%package libraries
%pattern_serverfunctions
Summary:        HPC Modularized Libraries
Group:          Metapackages
Provides:       pattern() = hpc_libraries
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2030
Provides:       pattern-visible()
Requires:       pattern() = hpc_compute_node

Requires:       lua-lmod
%include %{SOURCE1}

%description libraries
This package provides all the modularized libraries so that they can be used in an HPC environment. These libraries allow to install several MPI flavors in parallel.
In order to use these libraries one needs to load them via the module command first.

%files libraries
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/patterns-hpc-libraries.txt

################################################################################
%package development_node
%pattern_development
Summary:        HPC Development Packages
Group:          Metapackages
Provides:       pattern() = hpc_development_node
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 2040
Provides:       pattern-visible()
Requires:       pattern() = hpc_compute_node
Requires:       pattern() = hpc_libraries
Recommends:     python3-devel
Recommends:     pattern() = devel_C_C++
Recommends:     pattern() = devel_basis
Recommends:     pattern() = devel_perl
Recommends:     pattern() = devel_python3
Requires:       gnu-compilers-hpc-devel
Requires:       lua-lmod
# Ping is useful on compute nodes (bsc#1169484)
Requires:       iputils

# recommend additional development tools
Recommends:     cmake
Recommends:     gnuplot
Recommends:     gnuplot-doc
# include all the modularized stuff
%include %{SOURCE2}

%description development_node
This package provides all the relevant packages for developing HPC applications.
It depends on the pattern 'HPC Modularized Libraries'. In addition it includes the GNU compilers and the relevant management packages.

%files development_node
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/patterns-hpc-development_node.txt

################################################################################
%package workload_server
%pattern_serverfunctions
Summary:        HPC Workload Manager
Group:          Metapackages
Provides:       pattern() = hpc_workload_server
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-visible()

Requires:       slurm
Requires:       slurm-slurmdbd
# Ping is useful on compute nodes (bsc#1169484)
Requires:       iputils
Suggests:       mariadb

%description workload_server
This package provides all the relevant packages for running the central server
component of the slurm workload manager.

%files workload_server
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/patterns-hpc-workload_server.txt

%prep

%build

%install
mkdir -p "%{buildroot}%{_defaultdocdir}/patterns"
for pack in patterns-hpc-compute_node patterns-hpc-libraries \
        patterns-hpc-workload_server patterns-hpc-development_node; do
    echo "This file marks the pattern $pack in version %{version} to be installed." \
		>"%{buildroot}%{_defaultdocdir}/patterns/${pack}.txt"
done

%changelog
