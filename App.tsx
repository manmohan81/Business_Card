import React, { useState } from 'react';
import { Mail, Phone, MapPin, Linkedin, Globe, User, Briefcase, Award, Calendar, GraduationCap, Cog } from 'lucide-react';

function App() {
  const [isFlipped, setIsFlipped] = useState(false);

  const businessInfo = {
    name: "MANMOHAN SINGH RAWAT",
    title: "Design Manager",
    company: "Engineering Solutions Ltd.",
    email: "manmohan.rawat7@gmail.com",
    phone: "+91 98765 43210",
    location: "New Delhi, India",
    linkedin: "linkedin.com/in/manmohanrawat",
    website: "www.manmohanrawat.com",
    qualification: "B.E Mechanical Engineering",
    experience: "22 Years Experience",
    field: "Design & Development",
    specialties: ["Mechanical Design", "Product Development", "CAD/CAM Systems", "Project Management"],
    certifications: ["B.E Mechanical Engineering", "PMP Certified", "AutoCAD Professional", "SolidWorks Expert"]
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-indigo-900 flex">
      {/* Sidebar */}
      <div className="w-80 bg-black bg-opacity-20 backdrop-blur-lg p-6 space-y-6">
        <div className="text-center mb-8">
          <h2 className="text-xl font-bold text-white mb-2">Professional Expertise</h2>
          <div className="w-16 h-1 bg-gradient-to-r from-orange-500 to-red-500 mx-auto rounded-full"></div>
        </div>

        {/* Mechanical Design */}
        <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl p-6 text-white border border-white border-opacity-20">
          <div className="w-12 h-12 bg-orange-500 rounded-lg flex items-center justify-center mb-4">
            <Cog className="w-6 h-6 text-white" />
          </div>
          <h3 className="text-lg font-semibold mb-2">Mechanical Design</h3>
          <p className="text-sm text-blue-200 leading-relaxed">Expert in mechanical system design with 22 years of hands-on engineering experience.</p>
        </div>
        
        {/* Product Development */}
        <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl p-6 text-white border border-white border-opacity-20">
          <div className="w-12 h-12 bg-blue-500 rounded-lg flex items-center justify-center mb-4">
            <Briefcase className="w-6 h-6 text-white" />
          </div>
          <h3 className="text-lg font-semibold mb-2">Product Development</h3>
          <p className="text-sm text-blue-200 leading-relaxed">Comprehensive product development from concept to manufacturing with proven track record.</p>
        </div>
        
        {/* Technical Excellence */}
        <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl p-6 text-white border border-white border-opacity-20">
          <div className="w-12 h-12 bg-green-500 rounded-lg flex items-center justify-center mb-4">
            <GraduationCap className="w-6 h-6 text-white" />
          </div>
          <h3 className="text-lg font-semibold mb-2">Technical Excellence</h3>
          <p className="text-sm text-blue-200 leading-relaxed">B.E Mechanical Engineering foundation with advanced CAD/CAM and project management expertise.</p>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex items-center justify-center p-8">
        <div className="max-w-4xl w-full">
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-white mb-2">Professional Business Card</h1>
            <p className="text-blue-200">Click the card to flip and explore</p>
          </div>

          {/* Business Card Container */}
          <div className="perspective-1000">
            <div 
              className={`relative w-full max-w-2xl mx-auto transition-transform duration-700 transform-style-preserve-3d cursor-pointer ${
                isFlipped ? 'rotate-y-180' : ''
              }`}
              onClick={() => setIsFlipped(!isFlipped)}
            >
              {/* Front Side */}
              <div className="backface-hidden absolute inset-0 w-full h-96 bg-gradient-to-br from-white to-gray-50 rounded-2xl shadow-2xl border border-gray-200">
                <div className="h-full flex flex-col justify-between p-8">
                  {/* Header Section */}
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="w-16 h-16 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-full flex items-center justify-center mb-4">
                        <User className="w-8 h-8 text-white" />
                      </div>
                      <h2 className="text-2xl font-bold text-gray-800 mb-1">{businessInfo.name}</h2>
                      <p className="text-lg text-blue-600 font-medium">{businessInfo.title}</p>
                      <p className="text-gray-600">{businessInfo.company}</p>
                      <div className="flex items-center space-x-2 mt-2">
                        <GraduationCap className="w-4 h-4 text-green-600" />
                        <span className="text-sm text-gray-600">{businessInfo.qualification}</span>
                      </div>
                    </div>
                    <div className="text-right">
                      <div className="w-12 h-12 bg-gradient-to-br from-orange-500 to-red-500 rounded-lg flex items-center justify-center">
                        <Cog className="w-6 h-6 text-white" />
                      </div>
                    </div>
                  </div>

                  {/* Contact Information */}
                  <div className="space-y-3">
                    <div className="flex items-center space-x-3">
                      <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                        <Mail className="w-4 h-4 text-blue-600" />
                      </div>
                      <span className="text-gray-700 text-sm">{businessInfo.email}</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <div className="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                        <Phone className="w-4 h-4 text-green-600" />
                      </div>
                      <span className="text-gray-700 text-sm">{businessInfo.phone}</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <div className="w-8 h-8 bg-red-100 rounded-full flex items-center justify-center">
                        <MapPin className="w-4 h-4 text-red-600" />
                      </div>
                      <span className="text-gray-700 text-sm">{businessInfo.location}</span>
                    </div>
                  </div>

                  {/* Bottom Section */}
                  <div className="flex justify-between items-center">
                    <div className="flex space-x-3">
                      <div className="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center hover:bg-blue-700 transition-colors">
                        <Linkedin className="w-5 h-5 text-white" />
                      </div>
                      <div className="w-10 h-10 bg-gray-600 rounded-full flex items-center justify-center hover:bg-gray-700 transition-colors">
                        <Globe className="w-5 h-5 text-white" />
                      </div>
                    </div>
                    <p className="text-xs text-gray-500">Click to flip</p>
                  </div>
                </div>
              </div>

              {/* Back Side */}
              <div className="backface-hidden absolute inset-0 w-full h-96 bg-gradient-to-br from-orange-600 to-red-700 rounded-2xl shadow-2xl rotate-y-180">
                <div className="h-full flex flex-col justify-between p-8 text-white">
                  {/* Professional Details */}
                  <div>
                    <div className="flex items-center space-x-3 mb-6">
                      <Cog className="w-8 h-8 text-yellow-300" />
                      <h3 className="text-xl font-bold">Engineering Excellence</h3>
                    </div>
                    
                    <div className="space-y-4">
                      <div className="flex items-center justify-between">
                        <div className="flex items-center space-x-2">
                          <Calendar className="w-5 h-5 text-orange-200" />
                          <span className="font-medium">{businessInfo.experience}</span>
                        </div>
                        <div className="flex items-center space-x-2">
                          <Briefcase className="w-5 h-5 text-orange-200" />
                          <span className="font-medium">{businessInfo.field}</span>
                        </div>
                      </div>
                      
                      <div>
                        <h4 className="font-semibold mb-2 text-orange-200">Core Specialties:</h4>
                        <div className="grid grid-cols-2 gap-2">
                          {businessInfo.specialties.map((specialty, index) => (
                            <div key={index} className="bg-white bg-opacity-20 rounded-lg px-3 py-1">
                              <span className="text-sm">{specialty}</span>
                            </div>
                          ))}
                        </div>
                      </div>
                      
                      <div>
                        <h4 className="font-semibold mb-2 text-orange-200">Qualifications & Certifications:</h4>
                        <div className="space-y-1">
                          {businessInfo.certifications.map((cert, index) => (
                            <div key={index} className="flex items-center space-x-2">
                              <div className="w-2 h-2 bg-yellow-300 rounded-full"></div>
                              <span className="text-sm">{cert}</span>
                            </div>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Contact Links */}
                  <div className="space-y-2">
                    <div className="flex items-center space-x-3">
                      <Linkedin className="w-5 h-5 text-orange-200" />
                      <span className="text-sm">{businessInfo.linkedin}</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <Globe className="w-5 h-5 text-orange-200" />
                      <span className="text-sm">{businessInfo.website}</span>
                    </div>
                    <p className="text-xs text-orange-200 mt-4">Click to flip back</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;