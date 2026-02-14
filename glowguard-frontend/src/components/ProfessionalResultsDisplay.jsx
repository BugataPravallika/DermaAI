/**
 * PROFESSIONAL MEDICAL RESULTS DISPLAY COMPONENT
 * 
 * Displays:
 * - Top-3 differential diagnoses with confidence bars
 * - Medical recommendations and remedies
 * - Professional disclaimer
 * - Dermatologist guidance
 * 
 * Best Practices:
 * - Clear presentation of uncertainty (visual confidence bars)
 * - Prominent medical disclaimers
 * - Encourages professional consultation
 * - Responsive design for all devices
 */

import React, { useState } from 'react';
import { AlertCircle, ChevronDown, ChevronUp } from 'lucide-react';

const ProfessionalResultsDisplay = ({ results, onAnalyzeAnother }) => {
  const [expandedSection, setExpandedSection] = useState(null);

  if (!results || !results.analysis) {
    return <div className="text-center text-gray-500">No analysis results available</div>;
  }

  const toggleSection = (section) => {
    setExpandedSection(expandedSection === section ? null : section);
  };

  // Confidence bar component
  const ConfidenceBar = ({ confidence, disease }) => {
    const percentage = Math.round(confidence * 100);
    const getColor = (conf) => {
      if (conf >= 0.7) return 'bg-orange-500'; // High confidence = caution (medical)
      if (conf >= 0.5) return 'bg-yellow-500'; // Medium
      return 'bg-blue-500'; // Low confidence
    };

    return (
      <div className="mb-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
        <div className="flex justify-between items-center mb-2">
          <h3 className="font-semibold text-gray-800">{disease}</h3>
          <span className="text-lg font-bold text-gray-700">{percentage}%</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
          <div
            className={`h-full transition-all duration-500 ${getColor(confidence)}`}
            style={{ width: `${percentage}%` }}
          />
        </div>
        <p className="text-sm text-gray-600 mt-2">
          Confidence Score: {percentage}%
          {percentage < 50 && ' (Low confidence - consult dermatologist)'}
        </p>
      </div>
    );
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      {/* ========================================================================== */}
      {/* MEDICAL DISCLAIMER BOX (PROMINENT) */}
      {/* ========================================================================== */}
      <div className="mb-6 p-4 bg-red-50 border-l-4 border-red-500 rounded-r-lg">
        <div className="flex gap-3">
          <AlertCircle className="w-6 h-6 text-red-600 flex-shrink-0 mt-0.5" />
          <div>
            <h2 className="font-bold text-red-800 mb-2">⚠️ IMPORTANT MEDICAL DISCLAIMER</h2>
            <p className="text-sm text-red-700 leading-relaxed">
              <strong>This AI tool does NOT provide medical diagnosis.</strong> The results shown
              below are preliminary assessments for educational purposes only. Results must be
              reviewed by a qualified dermatologist or healthcare professional before any
              treatment decisions. If you notice any concerning skin changes, please consult a
              healthcare provider immediately.
            </p>
          </div>
        </div>
      </div>

      {/* ========================================================================== */}
      {/* TOP-3 DIFFERENTIAL DIAGNOSES SECTION */}
      {/* ========================================================================== */}
      <div className="mb-8">
        <h2 className="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
          <span>Possible Conditions (Differential Diagnosis)</span>
          <span className="text-sm text-gray-500 font-normal">(ranked by confidence)</span>
        </h2>

        {results.top_3_predictions && results.top_3_predictions.length > 0 ? (
          <div className="space-y-3">
            {results.top_3_predictions.map((pred, idx) => (
              <div key={idx} className="bg-white">
                <ConfidenceBar 
                  confidence={pred.confidence} 
                  disease={`${idx + 1}. ${pred.disease}`}
                />
              </div>
            ))}
          </div>
        ) : (
          <p className="text-gray-600">No prediction data available</p>
        )}
      </div>

      {/* ========================================================================== */}
      {/* PRIMARY DIAGNOSIS DETAILS */}
      {/* ========================================================================== */}
      <div className="mb-8 p-6 bg-blue-50 rounded-lg border border-blue-200">
        <h3 className="text-xl font-bold text-blue-900 mb-3">
          Primary Assessment: {results.analysis.disease_name}
        </h3>
        <p className="text-gray-700 leading-relaxed mb-4">
          {results.analysis.description}
        </p>

        {/* Severity Level */}
        <div className="mb-4 p-3 bg-white rounded border border-blue-100">
          <span className="text-sm text-gray-600">Assessed Severity Level: </span>
          <span className="font-semibold text-gray-800">
            {results.analysis.severity.charAt(0).toUpperCase() + results.analysis.severity.slice(1)}
          </span>
        </div>
      </div>

      {/* ========================================================================== */}
      {/* EXPANDABLE SECTIONS */}
      {/* ========================================================================== */}

      {/* Possible Causes */}
      <ExpandableSection
        title="Possible Causes"
        section="causes"
        expanded={expandedSection === 'causes'}
        onToggle={toggleSection}
        icon="🔍"
      >
        <ul className="list-disc list-inside space-y-2 text-gray-700">
          {results.analysis.causes && results.analysis.causes.length > 0 ? (
            results.analysis.causes.map((cause, idx) => (
              <li key={idx}>{cause}</li>
            ))
          ) : (
            <li>No specific causes identified</li>
          )}
        </ul>
      </ExpandableSection>

      {/* Remedies & Treatment */}
      <ExpandableSection
        title="Recommended Remedies & Care"
        section="remedies"
        expanded={expandedSection === 'remedies'}
        onToggle={toggleSection}
        icon="💊"
      >
        <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-4">
          <p className="text-sm text-green-900 mb-3">
            <strong>Note:</strong> These are general recommendations and should be discussed with
            a dermatologist before implementation.
          </p>
        </div>
        <ul className="space-y-3">
          {results.analysis.remedies && results.analysis.remedies.length > 0 ? (
            results.analysis.remedies.map((remedy, idx) => (
              <li
                key={idx}
                className="p-3 bg-gray-50 rounded-lg border-l-4 border-green-500 text-gray-700"
              >
                {remedy}
              </li>
            ))
          ) : (
            <li className="text-gray-600">No specific remedies available</li>
          )}
        </ul>
      </ExpandableSection>

      {/* Precautions */}
      <ExpandableSection
        title="Precautions & Prevention"
        section="precautions"
        expanded={expandedSection === 'precautions'}
        onToggle={toggleSection}
        icon="🛡️"
      >
        <ul className="space-y-3">
          {results.analysis.precautions && results.analysis.precautions.length > 0 ? (
            results.analysis.precautions.map((precaution, idx) => (
              <li
                key={idx}
                className="p-3 bg-gray-50 rounded-lg border-l-4 border-blue-500 text-gray-700"
              >
                {precaution}
              </li>
            ))
          ) : (
            <li className="text-gray-600">No specific precautions available</li>
          )}
        </ul>
      </ExpandableSection>

      {/* Diet Advice */}
      <ExpandableSection
        title="Dietary Recommendations"
        section="diet"
        expanded={expandedSection === 'diet'}
        onToggle={toggleSection}
        icon="🥗"
      >
        <DietAdviceDisplay dietAdvice={results.analysis.diet_advice} />
      </ExpandableSection>

      {/* Recommended Products */}
      {results.analysis.products && results.analysis.products.length > 0 && (
        <ExpandableSection
          title="Recommended Products"
          section="products"
          expanded={expandedSection === 'products'}
          onToggle={toggleSection}
          icon="🛒"
        >
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {results.analysis.products.map((product, idx) => (
              <div key={idx} className="p-4 bg-gray-50 rounded-lg border border-gray-200">
                <h4 className="font-semibold text-gray-800 mb-2">{product.name}</h4>
                <p className="text-sm text-gray-600 mb-2">{product.brand}</p>
                <p className="text-xs text-gray-500">{product.description}</p>
              </div>
            ))}
          </div>
        </ExpandableSection>
      )}

      {/* ========================================================================== */}
      {/* DERMATOLOGIST CONSULTATION BOX */}
      {/* ========================================================================== */}
      <div className="mt-8 p-6 bg-purple-50 rounded-lg border border-purple-200">
        <h3 className="font-bold text-purple-900 mb-3">✓ When to Consult a Dermatologist</h3>
        <ul className="space-y-2 text-sm text-purple-800">
          <li>• If symptoms persist longer than 2-3 weeks</li>
          <li>• If the condition worsens or spreads</li>
          <li>• If self-care measures don't help</li>
          <li>• If you develop new symptoms</li>
          <li>• If you're unsure about any diagnosis</li>
          <li>• For professional treatment options</li>
        </ul>
      </div>

      {/* ========================================================================== */}
      {/* ACTION BUTTONS */}
      {/* ========================================================================== */}
      <div className="mt-8 flex gap-4">
        <button
          onClick={onAnalyzeAnother}
          className="flex-1 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg transition-colors"
        >
          Analyze Another Image
        </button>
        <button
          onClick={() => window.print()}
          className="flex-1 px-6 py-3 bg-gray-600 hover:bg-gray-700 text-white font-semibold rounded-lg transition-colors"
        >
          Print Report
        </button>
      </div>

      {/* ========================================================================== */}
      {/* FOOTER DISCLAIMER */}
      {/* ========================================================================== */}
      <div className="mt-8 pt-6 border-t border-gray-200 text-xs text-gray-600 text-center">
        <p>
          GlowGuard is an AI screening tool only. It does not replace professional medical
          advice.
        </p>
        <p className="mt-2">
          For medical concerns, always consult with a qualified dermatologist or healthcare
          provider.
        </p>
      </div>
    </div>
  );
};

/**
 * Expandable Section Component
 */
const ExpandableSection = ({ title, section, expanded, onToggle, icon, children }) => {
  return (
    <div className="mb-4 border border-gray-200 rounded-lg overflow-hidden">
      <button
        onClick={() => onToggle(section)}
        className="w-full p-4 bg-gradient-to-r from-gray-50 to-gray-100 hover:from-gray-100 hover:to-gray-150 flex items-center justify-between transition-colors"
      >
        <span className="flex items-center gap-2 font-semibold text-gray-800">
          <span className="text-xl">{icon}</span>
          {title}
        </span>
        {expanded ? (
          <ChevronUp className="w-5 h-5 text-gray-600" />
        ) : (
          <ChevronDown className="w-5 h-5 text-gray-600" />
        )}
      </button>
      {expanded && <div className="p-4 bg-white">{children}</div>}
    </div>
  );
};

/**
 * Diet Advice Display Component
 */
const DietAdviceDisplay = ({ dietAdvice }) => {
  if (!dietAdvice) {
    return <p className="text-gray-600">No dietary recommendations available</p>;
  }

  // Handle if dietAdvice is a string
  if (typeof dietAdvice === 'string') {
    return <p className="text-gray-700 leading-relaxed">{dietAdvice}</p>;
  }

  // Handle if dietAdvice is an object
  if (typeof dietAdvice === 'object' && !Array.isArray(dietAdvice)) {
    const sections = Object.entries(dietAdvice);

    if (sections.length === 0) {
      return <p className="text-gray-600">No dietary recommendations available</p>;
    }

    return (
      <div className="space-y-4">
        {sections.map(([key, value], idx) => (
          <div key={idx} className="p-4 bg-gray-50 rounded-lg border-l-4 border-orange-500">
            <h4 className="font-semibold text-gray-800 mb-2 capitalize">
              {key.replace(/_/g, ' ')}
            </h4>
            <p className="text-gray-700">
              {typeof value === 'string' ? value : JSON.stringify(value)}
            </p>
          </div>
        ))}
      </div>
    );
  }

  return <p className="text-gray-700">{String(dietAdvice)}</p>;
};

export default ProfessionalResultsDisplay;
