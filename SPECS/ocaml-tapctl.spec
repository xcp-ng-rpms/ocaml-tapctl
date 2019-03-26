%global debug_package %{nil}

Name:           ocaml-tapctl
Version:        1.1.0
Release:        14%{?dist}
Summary:        Manipulate running tapdisk instances
License:        LGPL
URL:            https://github.com/xapi-project/tapctl
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/tapctl/archive?at=v%{version}&format=tar.gz&prefix=tapctl-%{version}#/tapctl-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/tapctl/archive?at=v1.1.0&format=tar.gz&prefix=tapctl-1.1.0#/tapctl-1.1.0.tar.gz) = c6eef52c1f30bdcdaf2d14bf215d5267d38116c1
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  xs-opam-repo
BuildRequires:  forkexecd-devel

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Manipulate running tapdisk instances on a xen host.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       forkexecd-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir /usr/lib/opamroot/system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc

%prep
%autosetup -p1 -n tapctl-%{version}

%build
make

%install
mkdir -p %{buildroot}%{ocaml_libdir}
mkdir -p %{buildroot}%{ocaml_docdir}
make install OPAM_PREFIX=%{buildroot}%{ocaml_dir} OPAM_LIBDIR=%{buildroot}%{ocaml_libdir}

%files
%doc ChangeLog
%doc LICENSE
%doc MAINTAINERS
%doc README.md
%{ocaml_libdir}/xapi-tapctl
%exclude %{ocaml_libdir}/xapi-tapctl/*.a
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmxa
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmxs
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmx
%exclude %{ocaml_libdir}/xapi-tapctl/*.mli
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmt
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmti

%files devel
%{ocaml_libdir}/xapi-tapctl/*.a
%{ocaml_libdir}/xapi-tapctl/*.cmx
%{ocaml_libdir}/xapi-tapctl/*.cmxa
%{ocaml_libdir}/xapi-tapctl/*.cmxs
%{ocaml_libdir}/xapi-tapctl/*.mli
%{ocaml_docdir}/xapi-tapctl

%changelog
* Wed Apr 04 2018 Marcello Seri <marcello.seri@citrix.com> - 1.1.0-6
- Update SPEC file to get rid of rpmbuild warnings

* Wed Jan 10 2018 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 1.1.0-1
- Ported build from oasis to jbuilder

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.1-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Wed Jun 22 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.1-1
- Update to 1.0.1

* Thu Apr 21 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Sat Apr 4 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.2-1
- Update to 0.9.2

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.1-2
- Split files correctly between base and devel packages

* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

