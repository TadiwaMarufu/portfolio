export default function SudokuBoard({ board }) {
  return (
    <div className="Board">
      {board.map((row, rowIndex) =>
        row.map((value, colIndex) => {
          let cellClass = "cell";

          if (colIndex === 2 || colIndex === 5) {
            cellClass += " box-right";
          }

          if (rowIndex === 2 || rowIndex === 5) {
            cellClass += " box-bottom";
          }

          return (
            <div
              className={cellClass}
              key={`${rowIndex}-${colIndex}`}
            >
              {value === 0 ? "" : value}
            </div>
          );
        })
      )}
    </div>
  );
}