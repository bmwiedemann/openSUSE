/**
 * Orthanc - A Lightweight, RESTful DICOM Store
 * Copyright (C) 2012-2016 Sebastien Jodogne, Medical Physics
 * Department, University Hospital of Liege, Belgium
 * Copyright (C) 2017-2019 Osimis S.A., Belgium
 *
 * This program is free software: you can redistribute it and/or
 * modify it under the terms of the GNU Affero General Public License
 * as published by the Free Software Foundation, either version 3 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Affero General Public License for more details.
 * 
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 **/


#include "DecodedImageAdapter.h"

#include "ViewerToolbox.h"

#include <Core/Images/ImageBuffer.h>
#include <Core/Images/ImageProcessing.h>
#include <Core/OrthancException.h>
#include <Core/Toolbox.h>
#include <Plugins/Samples/GdcmDecoder/OrthancImageWrapper.h>

#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string/predicate.hpp>
#include <json/writer.h>
#include <boost/regex.hpp>


namespace OrthancPlugins
{
  static bool GetStringTag(std::string& value,
                           const Json::Value& tags,
                           const std::string& tag)
  {
    if (tags.type() == Json::objectValue &&
        tags.isMember(tag) &&
        tags[tag].type() == Json::objectValue &&
        tags[tag].isMember("Type") &&
        tags[tag].isMember("Value") &&
        tags[tag]["Type"].type() == Json::stringValue &&
        tags[tag]["Value"].type() == Json::stringValue &&
        tags[tag]["Type"].asString() == "String")
    {
      value = tags[tag]["Value"].asString();
      return true;
    }        
    else
    {
      return false;
    }
  }
                                 

  static float GetFloatTag(const Json::Value& tags,
                           const std::string& tag,
                           float defaultValue)
  {
    std::string tmp;
    if (GetStringTag(tmp, tags, tag))
    {
      try
      {
        return boost::lexical_cast<float>(Orthanc::Toolbox::StripSpaces(tmp));
      }
      catch (boost::bad_lexical_cast&)
      {
      }
    }

    return defaultValue;
  }
                                 

  bool DecodedImageAdapter::ParseUri(CompressionType& type,
                                     uint8_t& compressionLevel,
                                     std::string& instanceId,
                                     unsigned int& frameIndex,
                                     const std::string& uri)
  {
    boost::regex pattern("^([a-z0-9]+)-([a-z0-9-]+)_([0-9]+)$");

    boost::cmatch what;
    if (!regex_match(uri.c_str(), what, pattern))
    {
      return false;
    }

    std::string compression(what[1]);
    instanceId = what[2];
    frameIndex = boost::lexical_cast<unsigned int>(what[3]);

    if (compression == "deflate")
    {
      type = CompressionType_Deflate;
    }
    else if (boost::starts_with(compression, "jpeg"))
    {
      type = CompressionType_Jpeg;
      int level = boost::lexical_cast<int>(compression.substr(4));
      if (level <= 0 || level > 100)
      {
        return false;
      }

      compressionLevel = static_cast<uint8_t>(level);
    }
    else
    {
      return false;
    }

    return true;
  }



  bool DecodedImageAdapter::Create(std::string& content,
                                   const std::string& uri)
  {
    std::string message = "Decoding DICOM instance: " + uri;
    OrthancPluginLogInfo(context_, message.c_str());

    CompressionType type;
    uint8_t level;
    std::string instanceId;
    unsigned int frameIndex;
    
    if (!ParseUri(type, level, instanceId, frameIndex, uri))
    {
      return false;
    }


    bool ok = false;

    Json::Value tags;
    std::string dicom;
    if (!GetStringFromOrthanc(dicom, context_, "/instances/" + instanceId + "/file") ||
        !GetJsonFromOrthanc(tags, context_, "/instances/" + instanceId + "/tags"))
    {
      throw Orthanc::OrthancException(Orthanc::ErrorCode_UnknownResource);
    }

    std::auto_ptr<OrthancImageWrapper> image(new OrthancImageWrapper(context_, OrthancPluginDecodeDicomImage(context_, dicom.c_str(), dicom.size(), frameIndex)));

    Json::Value json;
    if (GetCornerstoneMetadata(json, tags, *image))
    {
      if (type == CompressionType_Deflate)
      {
        ok = EncodeUsingDeflate(json, *image);
      }
      else if (type == CompressionType_Jpeg)
      {
        ok = EncodeUsingJpeg(json, *image, level);
      }
    }   

    if (ok)
    {
      std::string photometric;
      if (GetStringTag(photometric, tags, "0028,0004"))
      {
        json["Orthanc"]["PhotometricInterpretation"] = photometric;
      }
      
      Json::FastWriter writer;
      content = writer.write(json);
      return true;
    }
    else
    {
      char msg[1024];
      sprintf(msg, "Unable to decode the following instance: %s", uri.c_str());
      OrthancPluginLogWarning(context_, msg);
      return false;
    }
  }


  bool DecodedImageAdapter::GetCornerstoneMetadata(Json::Value& result,
                                                   const Json::Value& tags,
                                                   OrthancImageWrapper& image)
  {
    using namespace Orthanc;

    float windowCenter, windowWidth;

    Orthanc::ImageAccessor accessor;
    accessor.AssignReadOnly(OrthancPlugins::Convert(image.GetFormat()), image.GetWidth(),
                            image.GetHeight(), image.GetPitch(), image.GetBuffer());

    switch (accessor.GetFormat())
    {
      case PixelFormat_Grayscale8:
      case PixelFormat_Grayscale16:
      case PixelFormat_SignedGrayscale16:
      {
        int64_t a, b;
        Orthanc::ImageProcessing::GetMinMaxIntegerValue(a, b, accessor);
        result["minPixelValue"] = (a < 0 ? static_cast<int32_t>(a) : 0);
        result["maxPixelValue"] = (b > 0 ? static_cast<int32_t>(b) : 1);
        result["color"] = false;
        
        windowCenter = static_cast<float>(a + b) / 2.0f;
        
        if (a == b)
        {
          windowWidth = 256.0f;  // Arbitrary value
        }
        else
        {
          windowWidth = static_cast<float>(b - a) / 2.0f;
        }

        break;
      }

      case PixelFormat_RGB24:
      case PixelFormat_RGB48:
        result["minPixelValue"] = 0;
        result["maxPixelValue"] = 255;
        result["color"] = true;
        windowCenter = 127.5f;
        windowWidth = 256.0f;
        break;

      default:
        return false;
    }

    float slope = GetFloatTag(tags, "0028,1053", 1.0f);
    float intercept = GetFloatTag(tags, "0028,1052", 0.0f);

    result["slope"] = slope;
    result["intercept"] = intercept;
    result["rows"] = image.GetHeight();
    result["columns"] = image.GetWidth();
    result["height"] = image.GetHeight();
    result["width"] = image.GetWidth();

    bool ok = false;
    std::string pixelSpacing;
    if (GetStringTag(pixelSpacing, tags, "0028,0030"))
    {
      std::vector<std::string> tokens;
      Orthanc::Toolbox::TokenizeString(tokens, pixelSpacing, '\\');

      if (tokens.size() >= 2)
      {
        try
        {
          result["columnPixelSpacing"] = boost::lexical_cast<float>(Orthanc::Toolbox::StripSpaces(tokens[1]));
          result["rowPixelSpacing"] = boost::lexical_cast<float>(Orthanc::Toolbox::StripSpaces(tokens[0]));
          ok = true;
        }
        catch (boost::bad_lexical_cast&)
        {
        }
      }
    }

    if (!ok)
    {
      result["columnPixelSpacing"] = 1.0f;
      result["rowPixelSpacing"] = 1.0f;
    }

    result["windowCenter"] = GetFloatTag(tags, "0028,1050", windowCenter * slope + intercept);
    result["windowWidth"] = GetFloatTag(tags, "0028,1051", windowWidth * slope);

    return true;
  }


  static void ConvertRGB48ToRGB24(Orthanc::ImageAccessor& target,
                                  const Orthanc::ImageAccessor& source)
  {
    if (source.GetWidth() != target.GetWidth() ||
        source.GetHeight() != target.GetHeight())
    {
      throw Orthanc::OrthancException(Orthanc::ErrorCode_IncompatibleImageSize);
    }

    for (unsigned int y = 0; y < source.GetHeight(); y++)
    {
      const uint16_t* p = reinterpret_cast<const uint16_t*>(source.GetConstRow(y));
      uint8_t* q = reinterpret_cast<uint8_t*>(target.GetRow(y));

      for (unsigned int x = 0; x < source.GetWidth(); x++)
      {
        q[0] = p[0] >> 8;
        q[1] = p[1] >> 8;
        q[2] = p[2] >> 8;
        p += 3;
        q += 3;
      }
    }
  }


  bool  DecodedImageAdapter::EncodeUsingDeflate(Json::Value& result,
                                                OrthancImageWrapper& image)
  {
    Orthanc::ImageAccessor accessor;
    accessor.AssignReadOnly(OrthancPlugins::Convert(image.GetFormat()), image.GetWidth(),
                            image.GetHeight(), image.GetPitch(), image.GetBuffer());

    std::auto_ptr<Orthanc::ImageBuffer> buffer;

    Orthanc::ImageAccessor converted;

    switch (accessor.GetFormat())
    {
      case Orthanc::PixelFormat_RGB24:
        accessor.GetReadOnlyAccessor(converted);
        break;

      case Orthanc::PixelFormat_RGB48:
        buffer.reset(new Orthanc::ImageBuffer(Orthanc::PixelFormat_RGB24,
                                              accessor.GetWidth(),
                                              accessor.GetHeight(), false));
        buffer->GetWriteableAccessor(converted);
        ConvertRGB48ToRGB24(converted, accessor);
        break;

      case Orthanc::PixelFormat_Grayscale8:
      case Orthanc::PixelFormat_Grayscale16:
        buffer.reset(new Orthanc::ImageBuffer(Orthanc::PixelFormat_Grayscale16,
                                              accessor.GetWidth(),
                                              accessor.GetHeight(),
                                              true /* force minimal pitch */));
        buffer->GetWriteableAccessor(converted);
        Orthanc::ImageProcessing::Convert(converted, accessor);
        break;

      case Orthanc::PixelFormat_SignedGrayscale16:
        accessor.GetReadOnlyAccessor(converted);
        break;

      default:
        // Unsupported pixel format
        return false;
    }

    result["Orthanc"]["IsSigned"] = (accessor.GetFormat() == Orthanc::PixelFormat_SignedGrayscale16);

    // Sanity check: The pitch must be minimal
    assert(converted.GetSize() == converted.GetWidth() * converted.GetHeight() * 
           GetBytesPerPixel(converted.GetFormat()));
    result["Orthanc"]["Compression"] = "Deflate";
    result["sizeInBytes"] = converted.GetSize();

    std::string z;
    CompressUsingDeflate(z, image.GetContext(), converted.GetConstBuffer(), converted.GetSize());
    
    std::string s;
    Orthanc::Toolbox::EncodeBase64(s, z);
    result["Orthanc"]["PixelData"] = s;

    return true;
  }



  template <typename TargetType, typename SourceType>
  static void ChangeDynamics(Orthanc::ImageAccessor& target,
                             const Orthanc::ImageAccessor& source,
                             SourceType source1, TargetType target1,
                             SourceType source2, TargetType target2)
  {
    if (source.GetWidth() != target.GetWidth() ||
        source.GetHeight() != target.GetHeight())
    {
      throw Orthanc::OrthancException(Orthanc::ErrorCode_IncompatibleImageSize);
    }

    float scale = static_cast<float>(target2 - target1) / static_cast<float>(source2 - source1);
    float offset = static_cast<float>(target1) - scale * static_cast<float>(source1);

    const float minValue = static_cast<float>(std::numeric_limits<TargetType>::min());
    const float maxValue = static_cast<float>(std::numeric_limits<TargetType>::max());

    for (unsigned int y = 0; y < source.GetHeight(); y++)
    {
      const SourceType* p = reinterpret_cast<const SourceType*>(source.GetConstRow(y));
      TargetType* q = reinterpret_cast<TargetType*>(target.GetRow(y));

      for (unsigned int x = 0; x < source.GetWidth(); x++, p++, q++)
      {
        float v = (scale * static_cast<float>(*p)) + offset;

        if (v > maxValue)
        {
          *q = std::numeric_limits<TargetType>::max();
        }
        else if (v < minValue)
        {
          *q = std::numeric_limits<TargetType>::min();
        }
        else
        {
          //*q = static_cast<TargetType>(boost::math::iround(v));
          
          // http://stackoverflow.com/a/485546/881731
          *q = static_cast<TargetType>(floor(v + 0.5f));
        }
      }
    }
  }


  bool  DecodedImageAdapter::EncodeUsingJpeg(Json::Value& result,
                                             OrthancImageWrapper& image,
                                             uint8_t quality /* between 0 and 100 */)
  {
    Orthanc::ImageAccessor accessor;
    accessor.AssignReadOnly(OrthancPlugins::Convert(image.GetFormat()), image.GetWidth(),
                            image.GetHeight(), image.GetPitch(), image.GetBuffer());

    std::auto_ptr<Orthanc::ImageBuffer> buffer;

    Orthanc::ImageAccessor converted;

    if (accessor.GetFormat() == Orthanc::PixelFormat_Grayscale8 ||
        accessor.GetFormat() == Orthanc::PixelFormat_RGB24)
    {
      result["Orthanc"]["Stretched"] = false;
      accessor.GetReadOnlyAccessor(converted);
    }
    else if (accessor.GetFormat() == Orthanc::PixelFormat_RGB48)
    {
      result["Orthanc"]["Stretched"] = false;

      buffer.reset(new Orthanc::ImageBuffer(Orthanc::PixelFormat_RGB24,
                                            accessor.GetWidth(),
                                            accessor.GetHeight(), false));
      buffer->GetWriteableAccessor(converted);
      
      ConvertRGB48ToRGB24(converted, accessor);
    }
    else if (accessor.GetFormat() == Orthanc::PixelFormat_Grayscale16 ||
             accessor.GetFormat() == Orthanc::PixelFormat_SignedGrayscale16)
    {
      result["Orthanc"]["Stretched"] = true;

      buffer.reset(new Orthanc::ImageBuffer(Orthanc::PixelFormat_Grayscale8,
                                            accessor.GetWidth(),
                                            accessor.GetHeight(),
                                            true /* force minimal pitch */));
      buffer->GetWriteableAccessor(converted);

      int64_t a, b;
      Orthanc::ImageProcessing::GetMinMaxIntegerValue(a, b, accessor);
      result["Orthanc"]["StretchLow"] = static_cast<int32_t>(a);
      result["Orthanc"]["StretchHigh"] = static_cast<int32_t>(b);

      if (accessor.GetFormat() == Orthanc::PixelFormat_Grayscale16)
      {
        ChangeDynamics<uint8_t, uint16_t>(converted, accessor, a, 0, b, 255);
      }
      else
      {
        ChangeDynamics<uint8_t, int16_t>(converted, accessor, a, 0, b, 255);
      }
    }
    else
    {
      return false;
    }
    
    result["Orthanc"]["IsSigned"] = (accessor.GetFormat() == Orthanc::PixelFormat_SignedGrayscale16);
    result["Orthanc"]["Compression"] = "Jpeg";
    result["sizeInBytes"] = converted.GetSize();

    std::string jpeg;
    WriteJpegToMemory(jpeg, image.GetContext(), converted, quality);

    std::string s;
    Orthanc::Toolbox::EncodeBase64(s, jpeg);
    result["Orthanc"]["PixelData"] = s;
    
    return true;
  }
}
