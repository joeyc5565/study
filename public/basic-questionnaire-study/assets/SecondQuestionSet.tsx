import React, { useState } from 'react';

export const SecondQuestionSet: React.FC = () => {
    const [satisfaction, setSatisfaction] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        alert(Survey Completed! Satisfaction Level: ${satisfaction});
        // Redirect to the homepage or a results page after completion
        window.location.href = "/";
    };

    return (
        <div style={{ padding: "20px", fontFamily: "Arial" }}>
            <h2>Second Question Set</h2>
            <form onSubmit={handleSubmit}>
                <p>Rate your satisfaction with this survey from 1 (Not Enjoyable) to 5 (Very Enjoyable):</p>

                <label>
                    <input type="radio" name="satisfaction" value="1" onChange={(e) => setSatisfaction(e.target.value)} required /> 1
                </label>
                <label>
                    <input type="radio" name="satisfaction" value="2" onChange={(e) => setSatisfaction(e.target.value)} /> 2
                </label>
                <label>
                    <input type="radio" name="satisfaction" value="3" onChange={(e) => setSatisfaction(e.target.value)} /> 3
                </label>
                <label>
                    <input type="radio" name="satisfaction" value="4" onChange={(e) => setSatisfaction(e.target.value)} /> 4
                </label>
                <label>
                    <input type="radio" name="satisfaction" value="5" onChange={(e) => setSatisfaction(e.target.value)} /> 5
                </label>

                <button type="submit" style={{ padding: "10px", background: "green", color: "white", border: "none", marginTop: "10px" }}>
                    Submit
                </button>
            </form>
        </div>
    );
};
