# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_with check
%global debug_package %{nil}

%global crate paste

Name:           rust-paste
Version:        1.0.14
Release:        1
Summary:        Macros for all your token pasting needs
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/paste
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust >= 1.31
%if %{with check}
BuildRequires:  (crate(paste-test-suite/default) >= 0.0.0 with crate(paste-test-suite/default) < 1.0.0~)
BuildRequires:  (crate(rustversion/default) >= 1.0.0 with crate(rustversion/default) < 2.0.0~)
BuildRequires:  (crate(trybuild/default) >= 1.0.49 with crate(trybuild/default) < 2.0.0~)
BuildRequires:  (crate(trybuild/diff) >= 1.0.49 with crate(trybuild/diff) < 2.0.0~)
%endif

%global _description %{expand:
Macros for all your token pasting needs.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(paste) = 1.0.14
Requires:       cargo
Requires:       rust >= 1.31

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(paste/default) = 1.0.14
Requires:       cargo
Requires:       crate(paste) = 1.0.14

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
