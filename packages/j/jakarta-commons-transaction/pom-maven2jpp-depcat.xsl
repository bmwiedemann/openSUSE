<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:output method="xml" indent="yes" omit-xml-declaration="yes"/> 
 <xsl:strip-space elements="*"/> 
 <xsl:template match="*[name() != 'dependencies']|*/text()">
     <xsl:apply-templates/>
 </xsl:template>
 <xsl:template match="//dependencies">
  <xsl:for-each select="./dependency">
   <xsl:element name="dependency">
    <xsl:element name="maven">
     <xsl:choose>
      <xsl:when test="./groupId">
       <xsl:copy-of select="./groupId"/>
       <xsl:copy-of select="./artifactId"/>
      </xsl:when>
      <xsl:when test="./id">
       <xsl:choose>
        <xsl:when test="substring-before(./id/text(),':') != ''">
         <xsl:element name="groupId">
          <xsl:value-of select="substring-before(./id/text(),':')"/>
         </xsl:element>
         <xsl:element name="artifactId">
          <xsl:value-of select="substring-after(./id/text(),':')"/>
         </xsl:element>
        </xsl:when>
        <xsl:otherwise>
         <xsl:element name="groupId">
          <xsl:value-of select="./id/text()"/>
         </xsl:element>
         <xsl:element name="artifactId">
          <xsl:value-of select="./id/text()"/>
         </xsl:element>
        </xsl:otherwise>
       </xsl:choose>
      </xsl:when>
      <xsl:otherwise>
ERROR
      </xsl:otherwise>
     </xsl:choose>
     <xsl:for-each select="./*">
      <xsl:if test="(name() != 'groupId') and (name() != 'artifactId') and (name() != 'id')">
       <xsl:copy-of select="."/>
      </xsl:if>
     </xsl:for-each>
    </xsl:element>
    <xsl:element name="jpp">
     <xsl:element name="groupId">JPP</xsl:element>
     <xsl:choose>
      <xsl:when test="./artifactId">
       <xsl:copy-of select="./artifactId"/>
      </xsl:when>
      <xsl:when test="./id">
       <xsl:choose>
        <xsl:when test="substring-after(./id/text(),':') != ''">
         <xsl:element name="artifactId">
          <xsl:value-of select="substring-after(./id/text(),':')"/>
         </xsl:element>
        </xsl:when>
        <xsl:otherwise>
         <xsl:element name="artifactId">
          <xsl:value-of select="./id/text()"/>
         </xsl:element>
        </xsl:otherwise>
       </xsl:choose>
      </xsl:when>
      <xsl:otherwise>
ERROR
      </xsl:otherwise>
     </xsl:choose>
     <xsl:element name="jar">
      <xsl:choose>
       <xsl:when test="./artifactId">
        <xsl:value-of select="./artifactId/text()"/>
       </xsl:when>
       <xsl:when test="./id">
        <xsl:choose>
         <xsl:when test="substring-after(./id/text(),':') != ''">
          <xsl:value-of select="substring-after(./id/text(),':')"/>
         </xsl:when>
         <xsl:otherwise>
          <xsl:value-of select="./id/text()"/>
         </xsl:otherwise>
        </xsl:choose>
       </xsl:when>
       <xsl:otherwise>
ERROR
       </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
       <xsl:when test="./type">
        <xsl:choose>
         <xsl:when test="./type/text() = 'plugin'">.jar</xsl:when>
         <xsl:otherwise>.<xsl:value-of select="./type/text()"/></xsl:otherwise>
        </xsl:choose>
       </xsl:when>
       <xsl:otherwise>.jar</xsl:otherwise>
      </xsl:choose>
     </xsl:element>
     <xsl:for-each select="./*">
      <xsl:if test="(name() != 'groupId') and (name() != 'artifactId') and (name() != 'id')">
       <xsl:copy-of select="."/>
      </xsl:if>
     </xsl:for-each>
    </xsl:element>
   </xsl:element>
  </xsl:for-each>
 </xsl:template>
</xsl:stylesheet>
