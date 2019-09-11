<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:saxon="http://icl.com/saxon"
	extension-element-prefixes="saxon">
 <xsl:output method="xml" indent="yes" omit-xml-declaration="no"/> 
 <xsl:strip-space elements="*"/> 
 <xsl:template match="/" >
  <xsl:element name="depset">
   <saxon:group select="//dependency" group-by="./maven/artifactId">
    <xsl:sort select="./maven/artifactId"/>
    <xsl:element name="dependency">
     <xsl:element name="maven">
      <xsl:copy-of select="./maven/*[name() != 'properties']"/>
     </xsl:element>
     <xsl:element name="jpp">
      <xsl:copy-of select="./jpp/*[name() != 'properties']"/>
     </xsl:element>
    </xsl:element>
    <saxon:item/>
   </saxon:group>
  </xsl:element>
 </xsl:template>
</xsl:stylesheet>
