import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

function Editor(props) {
    return (<div className='component-padding'>
        <TextField
            label="Type Python Code"
            value={props.value}
            onChange={props.changeHandler}
            fullWidth
            multiline
            rows={15}
        />
        <Button
            variant="contained"
            id="request-button"
            onClick={props.onRequest}
        >
            Suggest Code!
        </Button>
    </div>)
}

export default Editor;