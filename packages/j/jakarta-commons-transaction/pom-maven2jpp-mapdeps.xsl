<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:param name="map" /> 
 <xsl:output method="xml" indent="yes" omit-xml-declaration="no"/> 
 <xsl:strip-space elements="*"/> 
 <xsl:template match="/project" >
  <xsl:element name="project">
   <xsl:copy-of select="child::*[not(self::dependencies)]"/>
   <xsl:if test="not(./dependencies)">
    <xsl:element name="dependencies">
     <xsl:for-each select="document($map)//add/dependency">
       <xsl:copy-of select="."/>
     </xsl:for-each>
    </xsl:element>
   </xsl:if>
   <xsl:apply-templates select="dependencies"/>
  </xsl:element>
 </xsl:template>
 <xsl:template match="dependencies" >
  <xsl:element name="dependencies">
   <xsl:for-each select="dependency">
    <xsl:if test="./artifactId">
     <xsl:call-template name="replace">
      <xsl:with-param name="artifact" select="./artifactId/text()"/>
     </xsl:call-template>
    </xsl:if>
    <xsl:if test="./id">
     <xsl:choose>
      <xsl:when test="substring-after(./id/text(),':') != ''">
       <xsl:call-template name="replace">
        <xsl:with-param name="artifact" select="substring-after(./id/text(),':')"/>
       </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
       <xsl:call-template name="replace">
        <xsl:with-param name="artifact" select="./id/text()"/>
       </xsl:call-template>
      </xsl:otherwise>
     </xsl:choose>
    </xsl:if>
   </xsl:for-each>
   <xsl:for-each select="document($map)//add/dependency">
    <xsl:copy-of select="."/>
   </xsl:for-each>
  </xsl:element>
 </xsl:template>
 <xsl:template name="replace">
  <xsl:param name="artifact"/>
  <xsl:variable name="this" select="."/>
  <xsl:element name="dependency">
   <xsl:choose>
    <xsl:when test="document($map)//dependency/maven[./artifactId/text() = $artifact]">
     <xsl:for-each select="document($map)//dependency/maven[./artifactId/text() = $artifact][1]">
      <xsl:copy-of select="../jpp/*"/>
      <xsl:copy-of select="$this/properties"/>
     </xsl:for-each>
    </xsl:when>
    <xsl:otherwise>
     <xsl:copy-of select="./*"/>
    </xsl:otherwise>
   </xsl:choose>
  </xsl:element>
  <xsl:if test="document($map)//dependency/maven[./artifactId/text() = $artifact]">
   <xsl:for-each select="document($map)//dependency/maven[./artifactId/text() = $artifact][1]">
    <xsl:for-each select="../add/dependency">
     <xsl:element name="dependency">
      <xsl:copy-of select="./*"/>
      <xsl:copy-of select="$this/properties"/>
     </xsl:element>
    </xsl:for-each>
   </xsl:for-each>
  </xsl:if>
 </xsl:template>
</xsl:stylesheet>
