import React, { useState } from 'react';

export const FirstQuestionSet: React.FC = () => {
    const [name, setName] = useState('');
    const [color, setColor] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        alert(Submitted: Name - ${name}, Favorite Color - ${color});
        // Redirect to the second question set
        window.location.href = "/second-question-set";
    };

    return (
        <div style={{ padding: "20px", fontFamily: "Arial" }}>
            <h2>First Question Set</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    What is your first name?
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                        placeholder="Enter your name"
                        style={{ display: "block", margin: "10px 0", padding: "5px" }}
                    />
                </label>

                <label>
                    What is your favorite color?
                    <select
                        value={color}
                        onChange={(e) => setColor(e.target.value)}
                        required
                        style={{ display: "block", margin: "10px 0", padding: "5px" }}
                    >
                        <option value="">Select a color</option>
                        <option value="red">Red</option>
                        <option value="blue">Blue</option>
                        <option value="green">Green</option>
                        <option value="yellow">Yellow</option>
                        <option value="other">Other</option>
                    </select>
                </label>

                <button type="submit" style={{ padding: "10px", background: "blue", color: "white", border: "none" }}>
                    Next
                </button>
            </form>
        </div>
    );
};
