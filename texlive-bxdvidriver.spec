%global tl_name bxdvidriver
%global tl_revision 79089

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Enables specifying a driver option effective only in DVI output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxdvidriver
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxdvidriver.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxdvidriver.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This single-function package enables authors to specify a global driver
option (dvips, dvipdfmx, etc) which is applied only when the engine
outputs a DVI file. It is useful to create special document- templates
that can be compiled in both PDF-mode and DVI-mode.

