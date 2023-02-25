import Button from '@mui/material/Button';

function Suggestion(props) {

    return (<>
        <Button
            variant="contained"
            id="clear-suggestions-button"
            color="warning"
            onClick={props.onClearSuggestions}
        >
            Clear Suggestions
        </Button>
        <div className="component-padding suggestion-component">
            {props.codeSuggestions.map((suggestion, id) => (
                <div key={id} className="suggestion-box">
                    {suggestion}
                </div>
            ))}
        </div>
    </>)
}

export default Suggestion;